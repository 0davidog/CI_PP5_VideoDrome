from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_basket, name='view_basket'),
    path('add/<video_id>/', views.add_to_basket, name='add_to_basket'),
    path('adjust/<video_id>/', views.update_basket, name='update_basket'),
    path('remove/<video_id>/', views.remove_from_basket, name='remove_from_basket'),
]