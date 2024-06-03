from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
import uuid

# Create your models here.


class Language(models.Model):
    """Model to represent different languages."""
    language = models.CharField(
        max_length=100, blank=True, null=True, unique=True
        )

    def __str__(self):
        """
        A string representation of the language track.
        """
        return f"{self.language}"


class Subtitle(models.Model):
    """Model to represent different subtitles."""
    subtitle = models.CharField(
        max_length=100, blank=True, null=True, unique=True
        )

    def __str__(self):
        """
        Function to return a string representation of the subtitle track name.
        """
        if self:
            return f"{self.subtitle}"
        else:
            return "No Information"


class Region(models.Model):
    """Model to represent different regions."""
    regioncode = models.CharField(
        max_length=100, blank=True, null=True, unique=True
        )
    region = models.CharField(
        max_length=100, blank=True, null=True
        )

    def __str__(self):
        """
        Function to return a string representation of the region code and region.
        """
        if self:
            return f"{self.regioncode}: {self.region}"
        else:
            return "No Information"


class Genre(models.Model):
    """Model to represent different genres."""
    genre_name = models.CharField(
        max_length=100, blank=True, null=True, unique=True
        )

    def __str__(self):
        """
        Function to return a string representation of the genre name.
        """
        if self:
            return f"{self.genre_name}"
        else:
            return "No Information"


class Video(models.Model):
    """Model to represent a video."""

    CERTIFICATE_CHOICES = [
        ("Not Rated", "Not Rated"),
        ("U", "U"),
        ("PG", "PG"),
        ("12", "12"),
        ("15", "15"),
        ("18", "18"),
    ]

    FORMAT_CHOICES = [
        ("DVD", "DVD"),
        ("Blu-Ray", "Blu-Ray"),
        ("UHD", "UHD"),
        ("Dual Format: Blu-Ray and DVD", "Dual Format: Blu-Ray and DVD"),
        ("Dual Format: UHD and Blu-Ray", "Dual Format: UHD and Blu-Ray"),
    ]

    CONDITION_CHOICES = [
        ("Used", "Used"),
        ("New", "New"),
    ]

    title = models.CharField(
        max_length=250, unique=True
        )
    slug = models.SlugField(
        max_length=250, editable=True
        )
    director = models.CharField(
        max_length=250, null=True
        )
    format = models.CharField(
        choices=FORMAT_CHOICES, max_length=250, default="DVD", null=False
        )
    discs = models.IntegerField(
        default=1, null=False
        )
    condition = models.CharField(
        choices=CONDITION_CHOICES, max_length=250, default="Used", null=True
        )
    price = models.DecimalField(
        default=0.0, null=False, max_digits=4, decimal_places=2
        )
    stock = models.IntegerField(
        default=0, null=False
        )
    cover = CloudinaryField(
        'video_cover', default='placeholder', null=True, blank=True
        )
    overview = models.TextField(blank=True)
    overview_source = models.URLField(blank=True, null=True)
    trailer = models.URLField(blank=True, null=True)
    release_year = models.DecimalField(
        max_digits=4, decimal_places=0, blank=True
        )
    certificate = models.CharField(
        choices=CERTIFICATE_CHOICES,
        max_length=250, default="Not Rated", null=False
        )
    aspect_ratio = models.CharField(max_length=250, blank=True)
    feature_length = models.CharField(max_length=250, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    on_sale = models.BooleanField(default=False)
    sku = models.CharField(max_length=254, null=True, blank=True)
    languages = models.ManyToManyField(
        Language, blank=True, related_name='video'
        )
    subtitles = models.ManyToManyField(
        Subtitle, blank=True, related_name='video'
        )
    region = models.ManyToManyField(
        Region, blank=True, related_name='video'
        )
    genre = models.ManyToManyField(Genre, blank=True)
    wishlist = models.ManyToManyField(
        User,
        related_name='wishlist',
        blank=True
    )

    def __str__(self):
        """
        Returns a string to identify model instance by title, year and format.
        """
        return f'{self.title} {self.release_year} {self.format}'

    def excerpt(self, num_words=25):
        """
        Returns a truncated version of overview text string.
        """
        # Split the text into words
        words = self.overview.split()

        # Get the partial text containing only the specified number of words
        excerpt = ' '.join(words[:num_words])

        return excerpt

    def in_stock(self):
        """
        Returns a different string value when the item stock is above 0
        """
        if self.stock > 0:
            return "In Stock"
        else:
            return "Out Of Stock"

    def stocked(self):
        """
        Returns a different boolean value when the item stock is above 0
        """
        if self.stock > 0:
            stocked = True
            return stocked
        else:
            stocked = False
            return stocked

    def _generate_sku(self):
        """
        Generate random 8 digit number using uuid
        """
        uuid_int = uuid.uuid4().int
        a = str(uuid_int)
        sku = a[:8]
        return sku

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the sku number
        if it hasn't been set already.
        """
        if not self.sku:
            self.sku = self._generate_sku()

        if not self.slug:
            self.slug = slugify(f"{self.title} {self.format}")

        super().save(*args, **kwargs)


class UserRating(models.Model):
    """Model to represent user ratings for a video."""
    RATING_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]
    video = models.ForeignKey(
        Video, on_delete=models.CASCADE, related_name="video_rating"
        )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_rating"
        )
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        """
        String representation of UserRating.
        """
        return f"{self.video} rated {self.rating} stars by {self.user}"


class UserReview(models.Model):
    """Model to represent user reviews for a video."""
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    title = models.CharField(max_length=250, blank=True)
    content = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviewer"
    )

    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        String representation of UserReview.
        """
        return f"Review: {self.content} by {self.author}"
