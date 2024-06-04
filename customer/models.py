from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField

# Create your models here.


# Define a model to represent customers
class Customer(models.Model):
    # Link to the corresponding user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Saved address details
    saved_street_address1 = models.CharField(
        max_length=80, null=True, blank=True
        )
    saved_street_address2 = models.CharField(
        max_length=80, null=True, blank=True
        )
    saved_town_or_city = models.CharField(
        max_length=40, null=True, blank=True
        )
    saved_county = models.CharField(
        max_length=80, null=True, blank=True
        )
    saved_postcode = models.CharField(
        max_length=20, null=True, blank=True
        )
    saved_country = CountryField(
        blank_label='Country *', null=True, blank=True
        )
    saved_phone_number = models.CharField(
        max_length=20, null=True, blank=True
        )

    # String representation of the object
    def __str__(self):
        return self.user.username


# Define a signal receiver
# to create or update customer info when a user is saved
@receiver(post_save, sender=User)
def create_or_update_customer_info(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    # Check if a new user is created
    if created:
        # If so, create a corresponding customer profile
        Customer.objects.create(user=instance)

    # For existing users, save the customer profile
    instance.customer.save()

