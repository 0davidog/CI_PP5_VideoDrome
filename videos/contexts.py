from .models import Genre


def genre_list(request):
    """
    Function to allow nav links to access genres.

    """

    genre_list = Genre.objects.all()

    context = {
        'genre_list': genre_list,
    }

    return context