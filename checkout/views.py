# Import necessary modules and functions from Django and other files
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from .forms import CustomerForm  
from .models import Customer, Order, VideoOrderItem, VideoOrderBasket
from videos.models import Video  
from basket.contexts import in_basket  # Importing bag_contents function

import stripe  # Importing the Stripe library for payment processing
import json  # Importing JSON library for working with JSON data

# View to handle caching checkout data
@require_POST
def cache_checkout_data(request):
    try:
        # Extracting payment ID from client secret
        pid = request.POST.get('client_secret').split('_secret')[0]

        stripe.api_key = settings.STRIPE_SECRET_KEY  # Setting Stripe API key

        # Modifying PaymentIntent metadata with basket content and other data
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })

        return HttpResponse(status=200)  # Returning HTTP response with status 200
    
    except Exception as e:
        # Handling exceptions and returning error message
        messages.error(request, 'Sorry, your payment cannot be processed right now. \
            Please try again later.')
        return HttpResponse(content=e, status=400)  # Returning error response with status 400

# View for checkout page
def checkout(request):
    
    stripe_public_key = settings.STRIPE_PUBLIC_KEY  # Getting Stripe public key from settings
    stripe_secret_key = settings.STRIPE_SECRET_KEY  # Getting Stripe secret key from settings

    if request.method == 'POST':  # If form is submitted
        
        basket = request.session.get('basket', {})  # Getting basket items from session

        # Getting customer form data from POST request
        form_data = {
            'f_name': request.POST['f_name'],
            'l_name': request.POST['l_name'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        customer_info = CustomerForm(form_data)  # Creating CustomerForm instance with form data

        if customer_info.is_valid():  # If customer form data is valid
            
            customer = customer_info.save(commit=False)  # Saving order form data to model
            pid = request.POST.get('client_secret').split('_secret')[0]  # Extracting payment ID  
            customer.save()  # Saving customer to database

            order = Order(
                customer=customer,
                stripe_pid = pid, # Setting Stripe payment ID for the order
                original_basket = json.dumps(basket), # Saving basket content as JSON string
            ) 
            order.save() # create order instance

            order_basket = VideoOrderBasket(
                order=order,
            ) 
            order_basket.save()
            # create basket model instance

            # Iterating through basket items and creating OrderVideoItem instances
            for item_id, quantity in basket.items():
                try:
                    video = Video.objects.get(id=item_id)  # Getting video from database

                    video_order_item = VideoOrderItem(
                                order=order,
                                video=video,
                                basket=order_basket,
                                quantity=quantity,
                            ) 
                    video_order_item.save()
                    # Saving order line item to database

                except Video.DoesNotExist:
                    # Handling case where video doesn't exist in database
                    messages.error(request, (
                        "Oh no, this video appears to not exist. Please contact us for assistance.")
                    )
                    order.delete()  # Deleting the order
                    return redirect(reverse('view_basket'))  # Redirecting to view basket page

            request.session['save_info'] = 'save-info' in request.POST  # Saving save_info to session
            # Redirecting to checkout success page with order number as argument
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            # Handling case where form data is invalid
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        basket = request.session.get('basket', {})  # Getting basket items from session
        if not basket:  # If basket is empty
            messages.error(request, "There's nothing in your basket at the moment")
            return redirect(reverse('videos'))  # Redirecting to videos page

        current_basket = in_basket(request)  # Getting basket contents using context processor

        total = current_basket['total_basket_cost']  # Getting total price from basket contents
        stripe_total = round(total * 100)  # Converting total to pence for Stripe

        stripe.api_key = stripe_secret_key  # Setting Stripe API key

        # Creating PaymentIntent with total amount and currency
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        customer_info = CustomerForm()  # Creating empty customer form

    if not stripe_public_key:  # If Stripe public key is missing
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'  # Template for checkout page

    context = {
        'customer_info': customer_info,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,  # Client secret for Stripe payment
    }

    return render(request, template, context)  # Rendering checkout page with context

# View for successful checkout
def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')  # Getting save_info from session
    order = get_object_or_404(Order, order_number=order_number)  # Getting order by order number

    # Displaying success message with order number and email
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.customer.email}.')

    if 'basket' in request.session:  # If basket exists in session
        del request.session['basket']  # Deleting bag from session

    template = 'checkout/checkout_successful.html'  # Template for checkout success page

    context = {
        'order': order,  # Passing order object to context
    }

    return render(request, template, context)  # Rendering checkout success page with context
