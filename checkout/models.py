import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField
from videos.models import Video

# Create your models here.

class Customer(models.Model):
    """Contact and Shipping information for order"""
    f_name = models.CharField(max_length=20, null=False, blank=False)
    l_name = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)


class Order(models.Model):
    """Create database entry of customer order"""
    order_number = models.UUIDField(default=uuid.uuid4(), null=False, editable=False)
    order_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer_order")
    charge = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_basket = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def cost(self, *args, **kwargs):
        self.charge = self.order_total
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.order_number} {self.order_date}"
    

class VideoOrderBasket(models.Model):
    """"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_total")
    order_sub_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    delivery = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def calculate_total(self, *args, **kwargs):
        """
        Sum up video sub toatals and add delivery to set the order total
        """
        self.order_sub_total = self.video_order.aggregate(sum('video_sub_total'))['video_sub_total__sum'] or 0
        self.delivery = 2.99
        self.order_total = self.order_sub_total + self.delivery
        super().save(*args, **kwargs)

    def __int__(self):
        return self.order_total


class VideoOrderItem(models.Model):
    """An entry for each unique video ordered"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="video_order_items")
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    basket = models.ForeignKey(VideoOrderBasket, on_delete=models.CASCADE, related_name="video_order")
    quantity = models.IntegerField(null=False, blank=False, default=0)
    video_sub_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the subtotal
        """
        self.video_sub_total = self.video.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.video.sku} on order {self.order.order_number}'


