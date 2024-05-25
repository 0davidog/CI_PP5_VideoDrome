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


class CustomerMessageThread(models.Model):
    """
    Model representing a thread of messages
    between a user and the customer service.
    """

    # Foreign key to link the thread to a user
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
        )

    # Email address of the user
    user_email = models.EmailField(
        max_length=254, null=False, blank=False
        )

    # Indicates if the thread is resolved
    is_resolved = models.BooleanField(default=False)

    # Order number associated with the thread (optional)
    order_number = models.CharField(
        max_length=32, null=True, blank=True
        )

    # Subject of the thread
    subject = models.CharField(
        max_length=254, null=False, blank=False
        )

    # Date when the thread was created
    created = models.DateField(auto_now_add=True)

    # Method to display whether the thread is resolved or not
    def resolved(self):
        """
        Returns a string indicating if the thread is resolved or not.
        """
        if self.is_resolved:
            return "| RESOLVED"
        else:
            return ""

    # String representation of the model
    def __str__(self):
        """
        Returns a string representation of the thread.
        """
        return f"{self.subject} | {self.created} {self.resolved()}"


class CustomerMessage(models.Model):
    """
    Model representing a customer message within a thread.
    """

    # Foreign key to link the message to a user
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
        )

    # Order number associated with the message (optional)
    order_number = models.CharField(
        max_length=32, null=True, blank=True
        )

    # Email address of the user
    user_email = models.EmailField(
        max_length=254, null=False, blank=False
        )

    # Subject of the message
    subject = models.CharField(
        max_length=254, null=False, blank=False
        )

    # Body of the message
    body = models.TextField(null=False, blank=False
                            )

    # Date and time when the message was sent
    date = models.DateTimeField(auto_now_add=True)

    # Foreign key to link the message to a thread
    thread = models.ForeignKey(
        CustomerMessageThread,
        on_delete=models.CASCADE,
        related_name='messages',
        null=True, blank=True)

    # String representation of the model
    def __str__(self):
        """
        Returns a string representation of the message.
        """
        return f"{self.user}: {self.subject}"
