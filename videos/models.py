from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Language(models.Model):
    """
    """
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.language

class Subtitle(models.Model):
    """
    """
    subtitle = models.CharField(max_length=100)

    def __str__(self):
        return self.subtitle

class Region(models.Model):
    """
    """
    regioncode = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.region

    
class Video(models.Model):
    """
    """
    
    CERTIFICATE_CHOICES=[
        ("1", "Not Rated"),
        ("2", "U"),
        ("3", "PG"),
        ("4", "12"),
        ("5", "15"),
        ("6", "18"),
    ]

    FORMAT_CHOICES=[
        ("DVD", "DVD"),
        ("Blu-Ray", "Blu-Ray"),
        ("4K Ultra HD", "4K Ultra HD"),
        ("Dual Format: Blu-Ray and DVD", "Dual Format: Blu-Ray and DVD"),
        ("Dual Format: UHD and Blu-Ray", "Dual Format: UHD and Blu-Ray"),
    ]
    
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, editable=True)
    certificate = models.CharField(choices=CERTIFICATE_CHOICES, max_length=250, default="1", null=False)
    format = models.CharField(choices=FORMAT_CHOICES, max_length=250, default="DVD", null=False)
    discs = models.IntegerField(default=1, null=False)
    price = models.DecimalField(default=0.0, null=False, max_digits=4, decimal_places=2)
    cover = models.ImageField(null=True, blank=True)
    cover_url = models.URLField(max_length=1024, null=True, blank=True)
    overview = models.TextField(max_length=500, blank=True)
    release_year = models.DecimalField(max_digits=4, decimal_places=0, blank=True)
    aspect_ratio = models.CharField(max_length=250, blank=True)
    feature_length = models.CharField(max_length=250, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    on_sale = models.BooleanField(default=False)
    sku = models.CharField(max_length=254, null=True, blank=True)
    languages = models.ManyToManyField(Language, blank=True)
    subtitles = models.ManyToManyField(Subtitle, blank=True)
    region = models.ManyToManyField(Region, blank=True)
    wishlist = models.ManyToManyField(
        User,
        related_name='wishlist',
        blank=True
    )

    def __str__(self):
        return f'{self.title} {self.release_year} {self.format}'


    
