from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from videos.models import Video


def view_checkout(request):
   
   """ Displays the checkout html template """
   
   return render(request, 'checkout/checkout.html')