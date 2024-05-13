from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField

# Create your models here.

class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    saved_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    saved_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    saved_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    saved_county = models.CharField(max_length=80, null=True, blank=True)
    saved_postcode = models.CharField(max_length=20, null=True, blank=True)
    saved_country = CountryField(blank_label='Country *', null=True, blank=True)
    saved_phone_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_customer_info(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    #if created:
    Customer.objects.create(user=instance)

    # Existing users: just save the profile
    #instance.customer.save()