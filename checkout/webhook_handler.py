# Import necessary modules and classes from Django and other apps
from django.http import HttpResponse
from django.conf import settings
from .email import send_confirmation_email  # Importing function to send confirmation email

from .models import CustomerOrder, OrderItem  # Importing models from the current app
from videos.models import Video  # Importing Video model from the videos app
from customer.models import Customer  # Importing Customer model from the customer app

import stripe  # Importing the Stripe library
import json  # Importing JSON module for JSON manipulation
import time  # Importing time module for handling time-related operations

# Define a class to handle Stripe webhooks
class StripeWH_Handler:
    """Handle Stripe webhooks"""

    # Constructor to initialize the handler with the request object
    def __init__(self, request):
        self.request = request

    # Method to handle generic webhook events
    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        print('generic handler reached')
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    # Method to handle successful payment intents
    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        print('intent.succeeded handler reached')

        # Extract relevant data from the event object
        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info
        latest_charge_id = event.data.object.latest_charge

        # Retrieve the charge object from the latest_charge_id
        latest_charge = stripe.Charge.retrieve(latest_charge_id)

        # Access the billing details from the charge object
        billing_details = latest_charge.billing_details
        shipping_details = intent.shipping

        # Calculate the grand total from the amount in cents
        grand_total = round(event.data.object.amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = Customer.objects.get(user__username=username)
            if save_info:
                profile.saved_phone_number = shipping_details.phone
                profile.saved_country = shipping_details.address.country
                profile.saved_postcode = shipping_details.address.postal_code
                profile.saved_town_or_city = shipping_details.address.city
                profile.saved_street_address1 = shipping_details.address.line1
                profile.saved_street_address2 = shipping_details.address.line2
                profile.saved_county = shipping_details.address.state
                profile.save()

        # Check if order already exists
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
        
        # If order exists, send confirmation email and return success response
        if order_exists:
            send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                # Create a new order if it doesn't exist
                order = CustomerOrder.objects.create(
                    name=shipping_details.name,
                    customer=profile,
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

                # Create order items for each video in the basket
                for item_id, quantity in json.loads(basket).items():
                    video = Video.objects.get(id=item_id)
                    order_line_item = OrderItem(
                        order=order,
                        video=video,
                        quantity=quantity,
                    )
                    order_line_item.save()

            except Exception as e:
                # Delete the order if creation fails and return error response
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        # Send confirmation email and return success response
        send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    # Method to handle failed payment intents
    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        print('intent failed')
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
