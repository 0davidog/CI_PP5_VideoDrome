import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField
from videos.models import Video
from customer.models import Customer

# Create your models here.


# Define a model to represent customer orders
class CustomerOrder(models.Model):
    # Fields representing order details
    order_number = models.CharField(max_length=32, null=False, editable=False)
    order_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='orders'
        )
    name = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
    )
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    original_basket = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default=''
    )

    # Method to generate a random, unique order number using UUID
    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    # Method to update the total cost of the order
    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        # Calculate order total
        self.order_total = self.orderitems.aggregate(
            Sum('video_sub_total')
            )['video_sub_total__sum'] or 0
        # Calculate delivery cost
        sdp = settings.STANDARD_DELIVERY_PERCENTAGE
        if self.order_total < settings.FREE_DELIVERY_OVER:
            self.delivery_cost = self.order_total * sdp / 100
        else:
            self.delivery_cost = 0
        # Calculate grand total
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    # Override the save method
    # to set the order number if it hasn't been set already
    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    # String representation of the object
    def __str__(self):
        return f"{self.order_number} {self.order_date}"


# Define a model for each unique item ordered in an order
class OrderItem(models.Model):
    """
    An entry for each unique video ordered
    """
    # Define a foreign key relationship with CustomerOrder model
    order = models.ForeignKey(
        CustomerOrder, on_delete=models.CASCADE, related_name="orderitems"
        )
    # Define a foreign key relationship with Video model
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    # Define a field to store the quantity of the ordered video
    quantity = models.IntegerField(null=False, blank=False, default=0)
    # Define a field to store the subtotal for the ordered video
    video_sub_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
        )

    def save(self, *args, **kwargs):
        """
        Override the save method to calculate the video subtotal before saving
        """
        # Calculate the video subtotal based on the video price and quantity
        self.video_sub_total = self.video.price * self.quantity
        # Call the parent class's save method to save the object
        super().save(*args, **kwargs)

    # Define a string representation for the object
    def __str__(self):
        return f'SKU {self.video.sku} on order {self.order.order_number}'
