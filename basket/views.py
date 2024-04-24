from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from videos.models import Video


def view_basket(request):
    """ A view that renders the bag contents page """

    return render(request, 'basket/basket.html')