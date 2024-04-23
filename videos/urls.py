from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_videos, name='videos'),
    path('<slug>', views.video_detail, name='video_detail'),
    path('wishlist/<slug:slug>/', views.wishlist, name='wishlist_video'),
    path('rating/<slug:slug>/<rating>', views.rating, name='rate_video'),
]