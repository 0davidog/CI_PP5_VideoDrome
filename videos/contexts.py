from .models import Genre


def genre_list(request):
    """
    View function to retrieve a list of genres.

    Args:
        request: HTTP request object.

    Returns:
        Dictionary containing genre list.

    """

    # Retrieve all genres from the database
    genre_list = Genre.objects.all()

    # Prepare context to pass to the template
    context = {
        'genre_list': genre_list,
        # List of genres to be accessed in the template
    }

    return context  # Return the context containing genre list
