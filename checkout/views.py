from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .forms import OrderForm
from videos.models import Video


def view_checkout(request):
   
   """ Displays the checkout html template """
   order_form = OrderForm()
   context = {
      'order_form': order_form,
   }
   return render(request, 'checkout/checkout.html', context)


def payment(request):
   """payment process"""

   return render(request, 'checkout/payment.html')