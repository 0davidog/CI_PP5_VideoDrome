from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_videos, name='videos'),
    path('<slug>', views.video_detail, name='video_detail'),
    path('wishlist/<slug:slug>/', views.wishlist, name='wishlist_video'),
    path('rating/<slug:slug>/<rating>', views.rating, name='rate_video'),
    path('review/<slug:slug>', views.create_review, name='create_review'),
    path('review/update/<slug:slug>/<review_id>', views.update_review, name='update_review'),
    path('review/delete/<review_id>', views.delete_review, name='delete_review'),
]