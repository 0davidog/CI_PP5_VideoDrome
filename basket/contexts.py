from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from videos.models import Video

def in_basket(request):

    basket_items = []
    total = 0
    video_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        video = get_object_or_404(Video, pk=item_id)
        total += quantity * video.price
        video_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'video': video,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    context = {
        'basket_items': basket_items,
        'total': total,
        'video_count': video_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context