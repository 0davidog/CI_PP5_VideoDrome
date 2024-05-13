from django.shortcuts import render, get_object_or_404
from .models import Customer

# Create your views here.

def customer_info(request):
    """
    """
    customer = get_object_or_404(Customer, user=request.user)

    context = {
        'customer': customer,
    }

    return render(request, 'customer/customer_info.html', context)