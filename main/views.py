from django.shortcuts import render

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
