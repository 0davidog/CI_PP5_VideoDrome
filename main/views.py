from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm

# Create your views here.


def index(request):
    """
    A view to return the index page.
    """

    # Flag indicating that the current page is the index page
    is_index = True

    # Context dictionary containing data to be passed to the template
    context = {
        'is_index': is_index,
    }

    # Render the index page with the provided context
    return render(request, 'main/index.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            send_mail(
                subject,
                message,
                email,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent.')
            return redirect('home')
        
        else:
            # If the form is not valid, add an error message
            messages.error(
                request,
                'Error submitting form. Please check your information.'
                )

    else:
        form = ContactForm()
    return render(request, 'main/contact_form.html', {'form': form})
