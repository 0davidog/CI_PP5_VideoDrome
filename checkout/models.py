import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField
from videos.models import Video

# Create your models here.

class CustomerOrder(models.Model):

    order_number = models.UUIDField(default=uuid.uuid4(), null=False, editable=False)
    order_date = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_basket = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
    
    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.orderitems.aggregate(Sum('video_sub_total'))['video_sub_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_OVER:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()


    def __str__(self):
        return f"{self.order_number} {self.order_date}"


class OrderItem(models.Model):
    """An entry for each unique video ordered"""
    order = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE, related_name="orderitems")
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    video_sub_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def save(self, *args, **kwargs):
        self.video_sub_total = self.video.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.video.sku} on order {self.order.order_number}'


