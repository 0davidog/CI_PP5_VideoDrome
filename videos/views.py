from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
from .models import Video, Language, Subtitle, UserRating, User, Genre

# Create your views here.

def all_videos(request):
    """ A view to show all products, including sorting and search queries """

    videos = Video.objects.all()
    search_query = None
    format_query = None
    genre_query = None

    if request.GET:
        
        if 'genre' in request.GET:
            genre_query = request.GET['genre']
            videos = videos.filter(genre__genre_name__icontains=genre_query)
            
        if 'format' in request.GET:
            format_query = request.GET['format']
            videos = videos.filter(format__icontains=format_query)

        if 's-q' in request.GET:
            search_query = request.GET['s-q']
            if not search_query:
                messages.error(request, "Search criteria needed!")
                return redirect(reverse('videos'))
            queries = Q(title__icontains=search_query)|Q(overview__icontains=search_query)|Q(director__icontains=search_query)

            videos = videos.filter(queries)

    context = {
        'videos': videos,
        'search': search_query,
        'genre_query': genre_query,
        'format_query': format_query,
    }

    return render(request, 'videos/videos.html', context)

def video_detail(request, slug):
    """
    """
    video = get_object_or_404(Video, slug=slug)
    languages = Language.objects.filter(video=video)
    subtitles = Subtitle.objects.filter(video=video)

    wishlisted = False
    user_rating = None
    if request.user.is_authenticated:
        if video.wishlist.filter(id=request.user.id).exists():
            wishlisted = True

        if UserRating.objects.filter(user=request.user, video=video).exists():
            user_rating = get_object_or_404(UserRating.objects.filter(user=request.user, video=video))
        else:
            user_rating = None

    context = {
        'video': video,
        'languages': languages,
        'subtitles': subtitles,
        'wishlisted': wishlisted,
        'user_rating': user_rating,
    }

    return render(request, 'videos/video_detail.html', context)

def wishlist(request, slug):
    """
    View for adding videos to a wishlist.
    Related to :model: `Video`
    """
    video = get_object_or_404(Video, slug=slug)
    if video.wishlist.filter(id=request.user.id).exists():
        video.wishlist.remove(request.user)
        messages.add_message(request, messages.SUCCESS, f"{video} removed from wishlist.")
    else:
        video.wishlist.add(request.user)
        messages.add_message(request, messages.SUCCESS, f"{video} added to wishlist.")
        
    return HttpResponseRedirect(reverse('video_detail', args=[slug]))


def rating(request, slug, rating):
    """
    View for rating videos
    """
    user = get_object_or_404(User, id=request.user.id)
    video = get_object_or_404(Video, slug=slug)
    user_rating = rating

    if UserRating.objects.filter(user=user, video=video).exists():
        rating_exists = get_object_or_404(UserRating.objects.filter(user=user, video=video))
        rating_exists.rating = user_rating
        rating_exists.save()
        messages.add_message(request, messages.SUCCESS, f"You rated {video} {user_rating} stars.")
    else:
        UserRating.objects.create(
            user=user,
            video=video,
            rating = user_rating,
        )
        messages.add_message(request, messages.SUCCESS, f"You rated {video} {user_rating} stars.")


    return HttpResponseRedirect(reverse('video_detail', args=[slug]))
