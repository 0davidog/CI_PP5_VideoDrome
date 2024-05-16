from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import CustomerOrderForm
from .models import CustomerOrder, OrderItem
from videos.models import Video
from customer.models import Customer
from customer.forms import SavedAddressForm
from basket.contexts import in_basket

import stripe
import json

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]

        stripe.api_key = settings.STRIPE_SECRET_KEY

        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})

        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = CustomerOrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_basket = json.dumps(basket)
            order.save()
            for item_id, quantity in basket.items():
                try:
                    video = Video.objects.get(id=item_id)
                
                    order_item = OrderItem(
                        order=order,
                        video=video,
                        quantity=quantity,
                    )
                    order_item.save()

                except Video.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your basket wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_basket'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, "There's nothing in your basket at the moment")
            return redirect(reverse('videos'))

        current_basket = in_basket(request)
        total = current_basket['total_basket_cost']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                
                customer = Customer.objects.get(user=request.user)

                order_form = CustomerOrderForm(initial={

                    'name': customer.user.get_full_name(),
                    'email': customer.user.email,
                    'phone': customer.saved_phone_number,
                    'country': customer.saved_country,
                    'postcode': customer.saved_postcode,
                    'town_or_city': customer.saved_town_or_city,
                    'street_address1': customer.saved_street_address1,
                    'street_address2': customer.saved_street_address2,
                    'county': customer.saved_county,
                })

            except Customer.DoesNotExist:
                order_form = CustomerOrderForm()
        
        else:
            order_form = CustomerOrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(CustomerOrder, order_number=order_number)
    order_items = OrderItem.objects.filter(order=order)

    if request.user.is_authenticated:

        customer = Customer.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.customer = customer
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'saved_phone_number': order.phone,
                'saved_country': order.country,
                'saved_postcode': order.postcode,
                'saved_town_or_city': order.town_or_city,
                'saved_street_address1': order.street_address1,
                'saved_street_address2': order.street_address2,
                'saved_county': order.county,
            }
            user_profile_form = SavedAddressForm(profile_data, instance=customer)
            if user_profile_form.is_valid():
                user_profile_form.save()
    
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'order_items': order_items,
    }

    return render(request, template, context)