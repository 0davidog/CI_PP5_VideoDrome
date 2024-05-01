from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from videos.models import Video


def view_basket(request):
    """ A view that renders the bag contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})
    video = get_object_or_404(Video.objects.filter(id=item_id))

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    messages.add_message(request, messages.SUCCESS, f"Added {video} to basket.")
    return redirect(redirect_url)
    


def update_basket(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})
    video = get_object_or_404(Video.objects.filter(id=item_id))

    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop(item_id)

    request.session['basket'] = basket
    if quantity == 0:
        messages.add_message(request, messages.SUCCESS, f"Removed {video} from basket.")
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """Remove the item from the shopping bag"""

    basket = request.session.get('basket', {})
    basket.pop(item_id)
    video = get_object_or_404(Video.objects.filter(id=item_id))

    request.session['basket'] = basket
    messages.add_message(request, messages.SUCCESS, f"Removed {video} from basket.")
    return redirect(reverse('view_basket'))
    