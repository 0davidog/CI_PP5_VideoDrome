from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Customer
from videos.models import Video, UserRating, UserReview
from .forms import SavedAddressForm, SavedDetailsForm
from checkout.models import CustomerOrder

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

    return render(request, 'customer/create_messages.html')

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



