from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_info, name='customer_info'),
    path('saved_address/', views.saved_address, name='saved_address'),
    path('update_info/', views.update_info, name='update_info'),
    path('view_wishlist/', views.view_wishlist, name='view_wishlist'),
    path('read_reviews/', views.read_reviews, name='read_reviews'),
    path(
        'order_detail/<order_number>',
        views.order_detail, name='order_detail'),
    path('inventory/', views.inventory, name='inventory'),
    path(
        'update_inventory/<video_id>',
        views.update_inventory, name='update_inventory'),
    path('orders', views.orders, name='orders'),
]
