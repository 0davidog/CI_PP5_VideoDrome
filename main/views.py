from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """

    is_index = True

    context = {
        'is_index': is_index,
    }

    return render(request, 'main/index.html', context)