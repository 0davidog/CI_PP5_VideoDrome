import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from videos.models import Video

# Create your models here.


class Order(models.Model):

    order_number = models.UUIDField(default=uuid.uuid4(), null=False, editable=False)
    order_date = models.DateTimeField(auto_now_add=True)

    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    basket_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)


    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.basket_total = self.order_basket.aggregate(Sum('basket_total'))['basket_total__sum']
        
        if self.basket_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.order_total = self.basket_total + self.delivery_cost
        self.save()

    def __str__(self):
        return self.order_number


class OrderBasket(models.Model):

    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='order_basket')
    basket_item = models.ForeignKey(Video, null=False, blank=False, on_delete=models.CASCADE)
    basket_quantity = models.IntegerField(null=False, blank=False, default=0)
    basket_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.basket_total = self.basket_item.price * self.basket_quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.basket_item.sku} on order {self.order.order_number}'