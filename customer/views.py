from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Customer
from checkout.models import CustomerOrder, OrderItem
from videos.models import Video, UserRating, UserReview
from .forms import SavedAddressForm, SavedDetailsForm

# Create your views here.


# Define a view function to display customer information
@login_required  # Ensure that only authenticated users can access this view
def customer_info(request):
    """
    View to display customer information and order history.
    """

    # Retrieve the customer object associated with the authenticated user
    customer = get_object_or_404(Customer, user=request.user)

    # Retrieve the order history of the customer
    order_history = CustomerOrder.objects.filter(
        customer=customer
        ).order_by('-order_date')

    # Create a context dictionary to pass data to the template
    context = {
        'customer': customer,
        'order_history': order_history,
    }

    # Render the 'customer_info.html' template with the context data
    return render(request, 'customer/customer_info.html', context)


# Define a view function to update user information
@login_required  # Ensure that only authenticated users can access this view
def update_info(request):
    """
    View to render and handle updating user information.
    """

    # Retrieve the authenticated user
    user = request.user

    # Check if the request method is POST (i.e., form submission)
    if request.method == 'POST':
        # Instantiate a SavedDetailsForm
        # with the POST data and the instance of the authenticated user
        saved_details_form = SavedDetailsForm(request.POST, instance=user)

        # Validate the submitted form data
        if saved_details_form.is_valid():
            # Save the updated user details
            # without committing it to the database
            saved_details = saved_details_form.save(commit=False)
            saved_details.save()
            # Add a success message
            # indicating the successful saving of the details
            messages.success(request, 'Your details have been saved.')
        else:
            # If the form is not valid, add an error message
            messages.error(
                request,
                'Error submitting form. Please check your information.'
                )
    else:
        # If the request method is not POST,
        # instantiate an empty SavedDetailsForm
        saved_details_form = SavedDetailsForm()

    # Create a context dictionary to pass data to the template
    context = {
        'user': user,
        'saved_details_form': saved_details_form,
    }

    # Render the 'update_info.html' template with the context data
    return render(request, 'customer/update_info.html', context)


# Define a view function to handle saving customer addresses
@login_required  # Ensure that only authenticated users can access this view
def saved_address(request):
    """
    View to render and handle saving customer addresses.
    """

    # Retrieve the customer object associated with the authenticated user
    customer = get_object_or_404(Customer, user=request.user)

    # Check if the request method is POST (i.e., form submission)
    if request.method == 'POST':
        # Instantiate a SavedAddressForm
        # with the POST data and the instance of the customer
        saved_address_form = SavedAddressForm(request.POST, instance=customer)

        # Validate the submitted form data
        if saved_address_form.is_valid():
            # Save the customer's address without committing it to the database
            saved_address = saved_address_form.save(commit=False)
            saved_address.save()
            # Add a success message
            # indicating the successful saving of the address
            messages.success(request, 'Your address has been saved.')
        else:
            # If the form is not valid, add an error message
            messages.error(
                request,
                'Error submitting form. Please check your information.'
                )
    else:
        # If the request method is not POST,
        # instantiate an empty SavedAddressForm
        saved_address_form = SavedAddressForm()

    # Create a context dictionary to pass data to the template
    context = {
        'customer': customer,
        'saved_address_form': saved_address_form,
    }

    # Render the 'saved_address.html' template with the context data
    return render(request, 'customer/saved_address.html', context)


# Define a view function to display user reviews
@login_required  # Ensure that only authenticated users can access this view
def read_reviews(request):
    """
    View to render and display user reviews.
    """

    # Retrieve star ratings given by the user
    star_ratings = UserRating.objects.filter(user=request.user)

    # Retrieve reviews written by the user
    user_reviews = UserReview.objects.filter(author=request.user)

    # Create a context dictionary to pass data to the template
    context = {
        'star_ratings': star_ratings,
        'user_reviews': user_reviews,
    }

    # Render the 'reviews.html' template with the context data
    return render(request, 'customer/reviews.html', context)


# Define a view function to read customer messages
# Ensure that only authenticated users can access this view
@login_required
def read_messages(request):
    """
    View to read customer messages in a specific thread.
    """

    # Get the threads associated with the user
    thread = CustomerMessageThread.objects.filter(user=request.user)

    # Initialize variables for storing customer messages and message query
    customer_messages = None
    message_query = None

    # Check if there are query parameters in the request
    if request.GET:
        # Get the thread ID from the request query parameters
        message_query = request.GET.get('thread')
        if message_query:
            # Filter messages by the specified thread and order by date
            customer_messages = CustomerMessage.objects.filter(
                thread=message_query
                ).order_by('-date')

    # Prepare the context for rendering the template
    context = {
        'customer_messages': customer_messages,
        # Customer messages in the specified thread
        'thread': thread,  # Threads associated with the user
        'message_query': message_query,  # ID of the thread being queried
    }

    # Render the 'read_messages.html' template with the context
    return render(request, 'customer/read_messages.html', context)


# Define a view function to display user's wishlist
@login_required  # Ensure that only authenticated users can access this view
def view_wishlist(request):
    """
    View to render and display user's wishlist.
    """

    # Initialize an empty list to store wishlist items
    wishlist = []

    # Retrieve all videos from the database
    videos = Video.objects.all()

    # Iterate through each video to check if it's in the user's wishlist
    for video in videos:
        # Check if the video is in the user's wishlist
        if video.wishlist.filter(id=request.user.id).exists():
            # If the video is in the wishlist, add it to the wishlist list
            wishlist.append(video)

    # Prepare the context for rendering the template
    context = {
        'wishlist': wishlist,  # List of videos in the user's wishlist
    }

    # Render the 'wishlist.html' template with the context
    return render(request, 'customer/wishlist.html', context)


# Define a view function to display order details
@login_required  # Ensure that only authenticated users can access this view
def order_detail(request, order_number):
    """
    View to render and display details of a specific order.
    """

    # Get the referer URL from the request metadata
    referer = request.META.get('HTTP_REFERER')

    # Check if an order with the given order number exists
    check = CustomerOrder.objects.filter(order_number=order_number)

    # If no order exists with the given order number
    if not check:
        # Add an error message indicating that no order was found
        messages.error(
                request,
                'Sorry. No Order with that number can be found.'
            )

        # If referer exists, redirect to it.
        # Otherwise, redirect to a default URL.
        if referer:
            return HttpResponseRedirect(referer)
        else:
            return HttpResponseRedirect('/')
            # Redirect to a default URL if no referer is found

    # Retrieve the order with the given order number
    order = get_object_or_404(CustomerOrder, order_number=order_number)

    # Retrieve the order items associated with the order
    order_items = OrderItem.objects.filter(order=order)

    # Prepare the context for rendering the template
    context = {
        'order': order,  # Details of the order
        'order_items': order_items,  # Items in the order
    }

    # Render the 'order_detail.html' template with the context
    return render(request, 'customer/order_detail.html', context)


# Define a view function to display inventory
@login_required  # Ensure that only authenticated users can access this view
def inventory(request):
    """
    View to render and display inventory.
    """

    # Get the referer URL from the request metadata
    referer = request.META.get('HTTP_REFERER')

    # Get the current user
    user = request.user

    # Retrieve all videos from the database and order them by title
    video_list = Video.objects.all().order_by('title')

    # Check if the user is not a staff member (i.e., not an admin)
    if not user.is_staff:
        # If the user is not a staff member, deny access to the page
        # If referer exists, redirect to it.
        # Otherwise, redirect to 'customer_info'
        if referer:
            messages.error(request, 'Sorry. This page is admin only.')
            return HttpResponseRedirect(referer)
        else:
            messages.error(request, 'Sorry. This page is admin only.')
            return HttpResponseRedirect('customer_info')

    # Prepare the context for rendering the template
    context = {
        'video_list': video_list,  # List of videos in the inventory
    }

    # Render the 'inventory.html' template with the context
    return render(request, 'customer/inventory.html', context)


# Define a view function to update inventory
@login_required  # Ensure that only authenticated users can access this view
def update_inventory(request, video_id):
    """
    View to update inventory information for a specific video.
    """

    # Check if the request method is POST (i.e., form submission)
    if request.method == "POST":
        # Retrieve the video object by its ID
        # or return a 404 error if not found
        video = get_object_or_404(Video.objects.filter(id=video_id))

        # Retrieve the submitted stock and price values from the form data
        # and convert them to integers
        stock = int(request.POST.get('stock'))
        price = int(request.POST.get('price'))

        # Update the stock and price attributes of the video object
        video.stock = stock
        video.price = price

        # Save the updated video object
        video.save()

    # Redirect the user to the inventory page
    return redirect(reverse('inventory'))


# Define a view function to display orders
@login_required  # Ensure that only authenticated users can access this view
def orders(request):
    """
    View to render and display orders.
    """

    # Get the referer URL from the request metadata
    referer = request.META.get('HTTP_REFERER')

    # Get the current user
    user = request.user

    # Retrieve all orders from the database and order them by order date
    order_list = CustomerOrder.objects.all().order_by('order_date')

    # Check if the user is not a staff member (i.e., not an admin)
    if not user.is_staff:
        # If the user is not a staff member, deny access to the page
        # If referer exists, redirect to it.
        # Otherwise, redirect to 'customer_info'
        if referer:
            messages.error(request, 'Sorry. This page is admin only.')
            return HttpResponseRedirect(referer)
        else:
            messages.error(request, 'Sorry. This page is admin only.')
            return HttpResponseRedirect('customer_info')

    # Prepare the context for rendering the template
    context = {
        'order_list': order_list,  # List of orders
    }

    # Render the 'orders.html' template with the context
    return render(request, 'customer/orders.html', context)
