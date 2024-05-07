import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from videos.models import Video

# Create your models here.


class Order(models.Model):

    order_number = models.UUIDField(default=uuid.uuid4(), null=False, editable=False)
    order_date = models.DateTimeField(auto_now_add=True)