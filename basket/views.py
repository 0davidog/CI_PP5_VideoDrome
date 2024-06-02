from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from videos.models import Video


def view_basket(request):

    """ Displays the basket html template """

    return render(request, 'basket/basket.html')


def add_to_basket(request, video_id):

    """ Add a quantity of the specified product to the shopping basket """

    quantity = int(request.POST.get('quantity'))
    # calls form number input by name 'quantity'
    # and converts submitted string to int
    redirect_url = request.POST.get('redirect_url')
    # retrieves redirect url from hidden input
    basket = request.session.get('basket', {})
    # sets basket variable in user session as empty dictionary (first use)
    # calls 'basket' dictionary from user session
    video = get_object_or_404(Video.objects.filter(id=video_id))
    # retrieve video added to basket by id

    if video_id in list(basket.keys()):
        # if id number of video already in 'basket' dictionary' as a key
        basket[video_id] += quantity
        # add to quantitiy of that video id
    else:
        basket[video_id] = quantity
        # else the quantity of the video is that given in request

    request.session['basket'] = basket
    # Adds aquired information to 'basket' dict in session

    messages.add_message(
        request, messages.SUCCESS, f"Added {video} to basket."
        )
    return redirect(redirect_url)


def update_basket(request, video_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    # calls form number input by name 'quantity'
    # and converts submitted string to int
    basket = request.session.get('basket', {})
    # calls 'basket' dictionary from user session
    video = get_object_or_404(Video.objects.filter(id=video_id))
    # retrieves video data by id number given in request

    if quantity > 0:
        # if quantity stated in request is greater than 0
        basket[video_id] = quantity
        # adjust quantity to number given
    else:
        # if quantity stated in request is 0
        basket.pop(video_id)
        # remove the item id from the basket

    request.session['basket'] = basket
    # update basket variable in session with data aquired

    if quantity == 0:
        messages.add_message(
            request, messages.SUCCESS, f"Removed {video} from basket."
            )
    else:
        messages.add_message(request, messages.SUCCESS, f"Basket updated.")

    return redirect(reverse('view_basket'))


def remove_from_basket(request, video_id):
    """Remove the item from the shopping bag"""

    basket = request.session.get('basket', {})
    # calls 'basket' dictionary from user session
    basket.pop(video_id)
    # removes item by id from basket dict
    video = get_object_or_404(Video.objects.filter(id=video_id))
    # retrive video information by id for confirmation message

    request.session['basket'] = basket
    # update basket dictionary in session with new information

    messages.add_message(
        request, messages.SUCCESS, f"Removed {video} from basket."
        )

    return redirect(reverse('view_basket'))
