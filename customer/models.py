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
    if created:
        Customer.objects.create(user=instance)

    # Existing users: just save the profile
    instance.customer.save()



class CustomerMessageThread(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_email = models.EmailField(max_length=254, null=False, blank=False)
    is_resolved = models.BooleanField(default=False)
    order_number = models.CharField(max_length=32, null=True, blank=True)
    subject = models.CharField(max_length=254, null=False, blank=False)
    created = models.DateField(auto_now_add=True)

    def resolved(self):
        if self.is_resolved:
            return "| RESOLVED"
        else:
            return ""
        
    def __str__(self):
        return f"{self.subject} | {self.created} {self.resolved()}"

class CustomerMessage(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=32, null=True, blank=True)
    user_email = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=254, null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    thread = models.ForeignKey(CustomerMessageThread, on_delete=models.CASCADE, related_name='messages', null=True, blank=True)

    def __str__(self):
        return f"{self.user}: {self.subject}"
