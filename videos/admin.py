from django.contrib import admin
from .models import Video, Language, Region, Subtitle, UserRating

# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title", "format"]}

admin.site.register(Video, VideoAdmin)
admin.site.register(Language)
admin.site.register(Region)
admin.site.register(Subtitle)
admin.site.register(UserRating)