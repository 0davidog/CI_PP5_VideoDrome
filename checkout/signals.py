from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import VideoOrderItem

@receiver(post_save, sender=VideoOrderItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update basket total on video order item update/create
    """
    instance.basket.calculate_total()

@receiver(post_delete, sender=VideoOrderItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update basket total on video order item delete
    """
    instance.basket.calculate_total()