from decimal import Decimal
from django.shortcuts import get_object_or_404
from django.conf import settings
from videos.models import Video

def in_basket(request):
    """Add to context, shopping basket data"""

    basket_items = []
    # empty list. Will be list of videos added to basket
    
    total_basket_cost = 0
    grand_total = 0
    # will be total cost of videos added to basket
     
    all_item_count = 0
    # will be total quantity of items in basket
    
    basket = request.session.get('basket', {}) 
    # calls basket variable in user session set in add to basket view

    for video_id, quantity in basket.items():
        # iterate through each video added to basket by id and quantity
        video = get_object_or_404(Video, pk=video_id)
        # retrieve video instance data
        sub_total = quantity * video.price
        # get sub total by multiplying video price by quantity
        total_basket_cost += quantity * video.price
        # add same sub total calculation to the total cost of basket list 
        all_item_count += quantity
        # add quantity of video to total quantity of basket list
        
        basket_items.append({
            'video_id': video_id,
            'quantity': quantity,
            'video': video,
            'sub_total': sub_total,
        }) # Add video and calculated information to basket list.

    if total_basket_cost < settings.FREE_DELIVERY_OVER:

        delivery = round(total_basket_cost * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100), 2)
        free_delivery_delta = settings.FREE_DELIVERY_OVER - total_basket_cost
    else:
        delivery = 0
        free_delivery_delta = 0
        
    grand_total = delivery + total_basket_cost

    context = {
        'basket_items': basket_items,
        'total_basket_cost': total_basket_cost,
        'all_item_count': all_item_count,
        'grand_total': grand_total,
        'free_delivery_delta': free_delivery_delta,
    } # Add basket list, total cost of the basket and count of all items in basket to context.

    return context # Make context available to entire app though conxent processor in settings