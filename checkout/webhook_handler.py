from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

from .models import CustomerOrder, OrderItem
from videos.models import Video
from customer.models import Customer


import json
import time

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        print('email?')
        cust_email = order.email

        subject = render_to_string(
            'checkout/email_confirmation/subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/email_confirmation/body.txt',
            {'order': order, 'contact_email': settings.EMAIL_HOST_USER})

        try:
            # Create EmailMessage object instead of using send_mail directly
            email = EmailMessage(subject, body, settings.EMAIL_HOST_USER, [cust_email])
            print(subject, body, settings.EMAIL_HOST_USER, [cust_email])
            email.send()
        except Exception as e:
            # Handle the exception
            # You can log the error, send a notification, or perform any necessary action
            print(f"Failed to send email to {cust_email}: {e}")

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

         # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            customer = Customer.objects.get(user__username=username)
            
            if save_info:
                customer.saved_phone_number = shipping_details.phone
                customer.saved_country = shipping_details.address.country
                customer.saved_postcode = shipping_details.address.postal_code
                customer.saved_town_or_city = shipping_details.address.city
                customer.saved_street_address1 = shipping_details.address.line1
                customer.saved_street_address2 = shipping_details.address.line2
                customer.saved_county = shipping_details.address.state
                customer.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = CustomerOrder.objects.get(
                    name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                order_exists = True
                break

            except CustomerOrder.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        
        else:
            order = None
            try:
                order = CustomerOrder.objects.create(
                    name__iexact=shipping_details.name,
                    customer=customer,
                    email=billing_details.email,
                    phone=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_basket=basket,
                    stripe_pid=pid,
                )

                for item_id, quantity in json.loads(basket).items():

                    video = Video.objects.get(id=item_id)

                    order_item = OrderItem(
                        order=order,
                        video=video,
                        quantity=quantity,
                    )
                    order_item.save()
                   

            except Exception as e:

                if order:
                    order.delete()

                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
            
        self._send_confirmation_email(order)

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)