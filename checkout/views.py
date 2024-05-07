from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
from .forms import OrderForm
from videos.models import Video


def checkout(request):
   """ Displays the checkout html template """
   
   basket = request.session.get('basket', {})
   
   if not basket:
      messages.error(request, "Your basket is empty!")
      return redirect(reverse('videos'))
   
   order_form = OrderForm()

   context = {
      'order_form': order_form,
      'stripe_public_key': 'pk_test_51PDqtEICDG3fo7DfpFtDCGolVfAeoawt9Ut98VbkS8Wl4rryj3CWaTc35HWHGliEg5Nv4g1L05vKt26Y5g7atGiS00yoi99Vpk',
      'client_secret': 'test client secret',
   }
   
   return render(request, 'checkout/checkout.html', context)
