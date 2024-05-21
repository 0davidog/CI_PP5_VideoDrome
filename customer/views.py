from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Customer
from videos.models import Video, UserRating, UserReview
from .forms import SavedAddressForm, SavedDetailsForm, MessageForm
from checkout.models import CustomerOrder
from customer.models import CustomerMessageThread, CustomerMessage

# Create your views here.

def customer_info(request):
    """
    """
    customer = get_object_or_404(Customer, user=request.user)
    order_history = CustomerOrder.objects.filter(customer=customer)

    context = {
        'customer': customer,
        'order_history': order_history,
    }

    return render(request, 'customer/customer_info.html', context)


def update_info(request):
    """
    """
    user = request.user

    if request.method == 'POST':
        saved_details_form = SavedDetailsForm(request.POST, instance=user)
        if saved_details_form.is_valid():
            saved_details = saved_details_form.save(commit=False)
            saved_details.save()
            messages.success(request, 'Your details have been saved.')
        else:
            messages.error(request, 'There was an error with your form. Please double check your information.')
    else:
        saved_details_form = SavedDetailsForm()
    
    saved_details_form = SavedDetailsForm()

    context = {
        'user': user,
        'saved_details_form': saved_details_form,
    }

    return render(request, 'customer/update_info.html', context)



def saved_address(request):
    
    customer = get_object_or_404(Customer, user=request.user)

    if request.method == 'POST':
        saved_address_form = SavedAddressForm(request.POST, instance=customer)
        if saved_address_form.is_valid():
            saved_address = saved_address_form.save(commit=False)
            saved_address.save()
            messages.success(request, 'Your address has been saved.')
        else:
            messages.error(request, 'There was an error with your form. Please double check your information.')
    else:
        saved_address_form = SavedAddressForm()
    
    saved_address_form = SavedAddressForm()

    context = {
        'customer': customer,
        'saved_address_form': saved_address_form,
    }

    return render(request, 'customer/saved_address.html', context)

def read_reviews(request):
    """
    """

    star_ratings = UserRating.objects.filter(user=request.user)
    user_reviews = UserReview.objects.filter(author=request.user)

    context = {
        'star_ratings': star_ratings,
        'user_reviews': user_reviews,
    }

    return render(request, 'customer/reviews.html', context)

def create_messages(request):
    """
    """
    if request.method == "POST":
        message_form = MessageForm(request.POST)

        if message_form.is_valid():
            message = message_form.save(commit=False)
            message.user = request.user
            message.thread = CustomerMessageThread.objects.create(
                user = request.user,
                order_number = message.order_number,
            )
            message.save()
            messages.success(request, 'Your message has been saved.')
            return redirect('read_messages')
        else:
            messages.error(request, 'There was an error with your form. Please double check your information.')

    else:
        message_form = MessageForm()


    context = {
        'message_form': message_form,
    }

    return render(request, 'customer/create_messages.html', context)

def read_messages(request):
    """
    """

    return render(request, 'customer/read_messages.html')


def view_wishlist(request):
    wishlist = []
    videos = Video.objects.all()

    for video in videos:
        if video.wishlist.filter(id=request.user.id).exists():
            wishlist.append(video)

    context = {
        'wishlist': wishlist,
    }

    return render(request, 'customer/wishlist.html', context)

def order_detail(request, order_number):
    """
    """
    

    return render(request, 'customer/order_detail.html')


