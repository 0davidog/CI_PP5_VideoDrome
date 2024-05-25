from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404, HttpResponse

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


# Define a view function to cache checkout data
@require_POST  # Ensure that only POST requests are allowed
def cache_checkout_data(request):
    """
    View to cache checkout data for a payment.
    """

    try:
        # Extract the payment intent ID from the client secret
        pid = request.POST.get('client_secret').split('_secret')[0]

        # Set the Stripe API key to the secret key from settings
        stripe.api_key = settings.STRIPE_SECRET_KEY

        # Modify the payment intent with metadata
        # including basket, save_info, and username
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            # Serialize the basket data to JSON
            'save_info': request.POST.get('save_info'),
            # Save info checkbox value
            'username': request.user,
            # Username of the authenticated user (if any)
        })

        # Return a success response with status code 200
        return HttpResponse(status=200)

    except Exception as e:
        # If an exception occurs,
        # display an error message and return a response with status code 400
        messages.error(
            request,
            'Sorry, your payment cannot be processed. Please try again later.'
            )
        return HttpResponse(content=e, status=400)


# Define a view function for the checkout process
def checkout(request):
    """
    View to handle the checkout process.
    """

    # Get the Stripe public key from settings
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    # Get the Stripe secret key from settings
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # Check if the request method is POST (i.e., form submission)
    if request.method == 'POST':
        # Retrieve the basket from the session
        basket = request.session.get('basket', {})

        # Extract form data from the request
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
        # Create an order form with the extracted form data
        order_form = CustomerOrderForm(form_data)

        # Check if the order form is valid
        if order_form.is_valid():
            # Save the order to the database
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_basket = json.dumps(basket)
            order.save()

            # Iterate over items in the basket and create order items
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
                        "A video in your basket wasn't found in our database."
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_basket'))

            # Set 'save_info' flag in session based on user input
            request.session['save_info'] = 'save-info' in request.POST

            # Redirect to the checkout success page
            # with the order number as a parameter
            return redirect(
                reverse('checkout_success', args=[order.order_number])
                )
        else:
            # If the order form is not valid, display an error message
            messages.error(
                request,
                'Error submitting form. Please check your information.'
                )
    else:
        # If the request method is not POST,
        # retrieve the basket from the session
        basket = request.session.get('basket', {})
        # If the basket is empty,
        # display a message and redirect to the videos page
        if not basket:
            messages.error(
                request,
                "There's nothing in your basket at the moment"
                )
            return redirect(reverse('videos'))

        # Calculate the total price of items in the basket
        current_basket = in_basket(request)
        total = current_basket['grand_total']
        # Convert the total price to the smallest currency unit (cents)
        stripe_total = round(total * 100)
        # Set the Stripe API key to the secret key from settings
        stripe.api_key = stripe_secret_key

        # Create a payment intent with the total amount
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Check if the user is authenticated
        if request.user.is_authenticated:
            try:
                # Attempt to retrieve customer details from the database
                customer = Customer.objects.get(user=request.user)

                # Initialize the order form with customer details
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
                # If customer details are not found, create an empty order form
                order_form = CustomerOrderForm()

        else:
            # If the user is not authenticated, create an empty order form
            order_form = CustomerOrderForm()

    # Display a warning message
    # if the Stripe public key is missing from settings
    if not stripe_public_key:
        messages.warning(
            request,
            (
                'Stripe public key is missing.'
                'Did you forget to set it in your environment?'
                )
            )

    # Set the template path
    template = 'checkout/checkout.html'
    # Prepare the context for rendering the template
    context = {
        'order_form': order_form,  # Order form
        'stripe_public_key': stripe_public_key,  # Stripe public key
        'client_secret': intent.client_secret,  # Payment intent client secret
    }

    # Render the template with the context
    return render(request, template, context)


# Define a view function for handling successful checkouts
def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """

    # Check if the 'save_info' flag is set in the session
    save_info = request.session.get('save_info')

    # Retrieve the order object based on the order number
    order = get_object_or_404(CustomerOrder, order_number=order_number)

    # Retrieve order items associated with the order
    order_items = OrderItem.objects.filter(order=order)

    # Check if the user is authenticated
    if request.user.is_authenticated:

        # Retrieve the customer object associated with the user
        customer = Customer.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.customer = customer
        order.save()

        # Save the user's info if 'save_info' flag is set
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
            # Create a form with profile data and save it
            user_profile_form = SavedAddressForm(
                profile_data, instance=customer
                )
            if user_profile_form.is_valid():
                user_profile_form.save()

    # Display a success message with order details
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    # Delete the 'basket' from the session
    if 'basket' in request.session:
        del request.session['basket']

    # Set the template path
    template = 'checkout/checkout_success.html'
    # Prepare the context for rendering the template
    context = {
        'order': order,  # Order object
        'order_items': order_items,  # Order items associated with the order
    }

    # Render the template with the context
    return render(request, template, context)
