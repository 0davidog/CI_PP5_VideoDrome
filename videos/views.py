from .forms import ReviewForm, VideoForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
from django.views.generic.base import TemplateView
from django.db.models.functions import Lower
from .models import Video, Language, Subtitle
from .models import UserRating, User, UserReview, Region


# Create your views here.

# Define a view function to handle requests for all videos
def all_videos(request):
    """ A view to show all videos, including sorting and search queries """

    # Retrieve all videos from the database
    # Ordered by the date they were added
    videos = Video.objects.filter(on_sale=True).order_by('-added')

    # Initialize variables for filtering and sorting
    all_videos = True
    search_query = None
    format_query = None
    genre_query = None
    sort = None
    direction = None
    current_sorting = None
    unsorted = True

    # Check if there are query parameters in the request
    if request.GET:

        # Check if sorting criteria are provided in the request
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            # If sorting by title,
            # annotate videos with lowercased title
            # for case-insensitive sorting
            if sortkey == 'title':
                sortkey = 'lower_title'
                videos = videos.annotate(lower_title=Lower('title'))
            unsorted = False

            # Check if sorting direction is provided in the request
            if 'direction' in request.GET:
                direction = request.GET['direction']

                # Adjust sorting key based on direction
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
                unsorted = False

            # Apply sorting to videos based on the sorting key
            videos = videos.order_by(sortkey)

        # Check if genre filter is provided in the request
        if 'genre' in request.GET:
            genre_query = request.GET['genre']

            # Filter videos based on genre query
            if genre_query == "4k,ultra,hd,uhd":
                genre_query.split(',')
                videos = videos.filter(
                    genre__genre_name__icontains=genre_query
                    )
                all_videos = False
            else:
                videos = videos.filter(
                    genre__genre_name__icontains=genre_query
                    )
                all_videos = False

        # Check if format filter is provided in the request
        if 'format' in request.GET:
            format_query = request.GET['format']

            # Filter videos based on format query
            videos = videos.filter(format__icontains=format_query)
            all_videos = False

        # Check if search query is provided in the request
        if 's-q' in request.GET:
            search_query = request.GET['s-q']

            # If no search query is provided, display an error message
            if not search_query:
                messages.error(request, "Search criteria needed!")
                return redirect(reverse('videos'))

            # Define queries
            # to search for the provided search query
            # in title, overview, and director fields
            queries = Q(
                title__icontains=search_query
                ) | Q(
                    overview__icontains=search_query
                    ) | Q(
                        director__icontains=search_query
                        )

            # Filter videos based on search queries
            videos = videos.filter(queries)
            all_videos = False

        # Set the current sorting criteria for display in the template
        current_sorting = f"{sort}_{direction}"

    # Create a context dictionary to pass data to the template
    context = {
        'videos': videos,
        'all_videos': all_videos,
        'search': search_query,
        'genre_query': genre_query,
        'format_query': format_query,
        'current_sorting': current_sorting,
        'unsorted': unsorted,
    }

    # Render the 'videos.html' template with the context data
    return render(request, 'videos/videos.html', context)


# Define a view function to handle requests for video details
def video_detail(request, slug):
    """
    View function to display details of a video.
    """

    # Retrieve the video object with the provided slug from the database
    video = get_object_or_404(Video, slug=slug)

    # Retrieve related languages, subtitles, and regions for the video
    languages = Language.objects.filter(video=video)
    subtitles = Subtitle.objects.filter(video=video)
    region = Region.objects.filter(video=video)

    # Initialize variables for user-specific information
    wishlisted = False
    user_rating = None
    user_reviews = None
    review_rating = 0
    review_count = 0
    one_star_ratings = 0
    two_star_ratings = 0
    three_star_ratings = 0
    four_star_ratings = 0
    five_star_ratings = 0

    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Check if the video is wishlisted by the user
        if video.wishlist.filter(id=request.user.id).exists():
            wishlisted = True

        # Check if the user has rated the video
        if UserRating.objects.filter(user=request.user, video=video).exists():
            user_rating = get_object_or_404(
                UserRating.objects.filter(user=request.user, video=video)
                )
        else:
            user_rating = None

    # Check if there are any user reviews for the video
    if UserReview.objects.filter(video=video, approved=True).exists():
        user_reviews = UserReview.objects.filter(video=video)
        review_count = user_reviews.count()

        # Calculate average review rating
        for review in user_reviews:
            if UserRating.objects.filter(
                user=review.author, video=video
            ).exists():
                review_rating = get_object_or_404(
                    UserRating.objects.filter(
                        user=review.author, video=video
                    )
                )
            else:
                review_rating = 0
    else:
        user_reviews = None

    # Calculate count of ratings for each star
    one_star_ratings = UserRating.objects.filter(
        video=video, rating=1
        ).count()
    two_star_ratings = UserRating.objects.filter(
        video=video, rating=2
        ).count()
    three_star_ratings = UserRating.objects.filter(
        video=video, rating=3
        ).count()
    four_star_ratings = UserRating.objects.filter(
        video=video, rating=4
        ).count()
    five_star_ratings = UserRating.objects.filter(
        video=video, rating=5
        ).count()

    # Create a context dictionary to pass data to the template
    context = {
        'video': video,
        'languages': languages,
        'subtitles': subtitles,
        'wishlisted': wishlisted,
        'user_rating': user_rating,
        'user_reviews': user_reviews,
        'review_rating': review_rating,
        'review_count': review_count,
        'one_star_ratings': one_star_ratings,
        'two_star_ratings': two_star_ratings,
        'three_star_ratings': three_star_ratings,
        'four_star_ratings': four_star_ratings,
        'five_star_ratings': five_star_ratings,
        'region': region,
    }

    # Render the 'video_detail.html' template with the context data
    return render(request, 'videos/video_detail.html', context)


# Define a view function to handle adding/removing videos from wishlist
def wishlist(request, slug):
    """
    View for adding videos to a wishlist.
    Related to :model: `Video`
    """

    # Retrieve the video object with the provided slug from the database
    video = get_object_or_404(Video, slug=slug)

    # Check if the video is already in the user's wishlist
    if video.wishlist.filter(id=request.user.id).exists():
        # If the video is in the wishlist, remove it
        video.wishlist.remove(request.user)
        # Add a success message indicating the removal from the wishlist
        messages.add_message(
            request, messages.SUCCESS, f"{video} removed from wishlist."
            )
    else:
        # If the video is not in the wishlist, add it
        video.wishlist.add(request.user)
        # Add a success message indicating the addition to the wishlist
        messages.add_message(
            request, messages.SUCCESS, f"{video} added to wishlist."
            )

    # Redirect the user to the video detail page
    # after adding/removing from wishlist
    return HttpResponseRedirect(reverse('video_detail', args=[slug]))


# Define a view function to handle rating videos
def rating(request, slug, rating):
    """
    View for rating videos
    """

    # Retrieve the authenticated user object
    user = get_object_or_404(User, id=request.user.id)

    # Retrieve the video object with the provided slug from the database
    video = get_object_or_404(Video, slug=slug)

    # Convert the rating parameter to an integer
    user_rating = int(rating)

    # Check if the user has already rated the video
    if UserRating.objects.filter(user=user, video=video).exists():
        # If the user has already rated the video, update their existing rating
        rating_exists = get_object_or_404(UserRating.objects.filter(
            user=user, video=video
            ))
        rating_exists.rating = user_rating
        rating_exists.save()
        # Add a success message indicating the updated rating
        messages.add_message(
            request, messages.SUCCESS,
            f"You rated {video} {user_rating} stars."
            )
    else:
        # If the user has not rated the video, create a new rating entry
        UserRating.objects.create(
            user=user,
            video=video,
            rating=user_rating,
        )
        # Add a success message indicating the new rating
        messages.add_message(
            request, messages.SUCCESS,
            f"You rated {video} {user_rating} stars."
            )

    # Redirect the user to the video detail page after rating
    return HttpResponseRedirect(reverse('video_detail', args=[slug]))


# Define a view function to render and submit a review form
def create_review(request, slug):
    """
    View to render and submit a review form.
    """

    # Instantiate a new review form
    review_form = ReviewForm()

    # Retrieve the authenticated user object
    user = get_object_or_404(User, id=request.user.id)

    # Retrieve the video object with the provided slug from the database
    video = get_object_or_404(Video, slug=slug)

    # Initialize variable for user rating
    user_rating = None

    # Check if the user has already submitted a review for the video
    review = UserReview.objects.filter(
        author=request.user, video=video
        ).first()
    if review:
        # If a review exists, redirect to the update review page
        slug = video.slug
        review_id = review.id
        messages.add_message(
            request, messages.WARNING,
            f"You can only write one review per title. Edit your review?"
            )
        return redirect(reverse('update_review', args=[slug, review_id]))

    # Check if the request method is POST (i.e., form submission)
    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        # Validate the submitted review form
        if review_form.is_valid():
            # Save the review object without committing it to the database
            review = review_form.save(commit=False)
            review.author = user
            review.video = video
            review.save()
            # Add a success message indicating the submission of the review
            messages.add_message(
                request, messages.SUCCESS,
                f"Review submitted. Awaiting admin approval."
                )
            # Clear the form for a new review
            review_form = ReviewForm()
            # Redirect the user to the video detail page
            return HttpResponseRedirect(reverse('video_detail', args=[slug]))
        else:
            # If the form is not valid, add an error message
            messages.add_message(
                request, messages.ERROR,
                f"Review failed to submit. Please check form."
                )

    # Check if the user has already rated the video
    if UserRating.objects.filter(user=request.user, video=video).exists():
        user_rating = get_object_or_404(
            UserRating.objects.filter(
                user=request.user, video=video
                )
            )
    else:
        user_rating = None

    # Create a context dictionary to pass data to the template
    context = {
        "video": video,
        "review_form": review_form,
        "user_rating": user_rating,
    }

    # Render the 'create_review.html' template with the context data
    return render(request, "videos/create_review.html", context)


# Define a view function to handle updating a review
def update_review(request, slug, review_id):
    """
    View to render and submit an updated review form.
    """

    # Retrieve the video object with the provided slug from the database
    video = get_object_or_404(Video, slug=slug)

    # Retrieve the review object with the provided review_id from the database
    review = get_object_or_404(UserReview, id=review_id)

    # Check if the request method is POST (i.e., form submission)
    if request.method == 'POST':
        # Instantiate a review form with the POST data
        # and the instance of the existing review
        review_form = ReviewForm(data=request.POST, instance=review)

        # Validate the submitted review form
        # and check if the author is the current user
        if review_form.is_valid() and review.author == request.user:
            # Save the updated review object
            # without committing it to the database
            review = review_form.save(commit=False)
            review.video = video
            review.approved = False  # Flag the review as not approved
            review.save()
            # Add a success message
            # indicating the submission of the review edit
            messages.add_message(
                request, messages.SUCCESS,
                f"Review edit submitted. Awaiting admin approval."
                )
            # Clear the form for a new review
            review_form = ReviewForm()
            # Redirect the user to the video detail page
            return HttpResponseRedirect(reverse('video_detail', args=[slug]))
        else:
            # If the form is not valid
            # or the user is not the author,
            # add an error message
            messages.add_message(
                request, messages.ERROR,
                f"Review failed to submit. Please check form."
                )

    else:
        # If the request method is not POST,
        # instantiate a review form with the existing review instance
        review_form = ReviewForm(instance=review)

    # Create a context dictionary to pass data to the template
    context = {
        "video": video,
        "review_form": review_form,
    }

    # Render the 'create_review.html' template with the context data
    return render(request, "videos/create_review.html", context)


# Define a view function to handle deleting a review
def delete_review(request, review_id):
    """
    View to handle deleting a review.
    """

    # Retrieve the referer URL from the request headers
    referer = request.META.get('HTTP_REFERER')

    # Retrieve the review object with the provided review_id from the database
    review = get_object_or_404(UserReview, id=review_id)

    # Check if the currently logged-in user is the author of the review
    if request.user == review.author:
        # If the user is the author, delete the review
        review.delete()
        # Add a success message
        # indicating the successful deletion of the review
        messages.add_message(
            request, messages.SUCCESS,
            f"Review successfully deleted."
            )
    else:
        # If the user is not the author, add an error message
        messages.add_message(
            request, messages.ERROR,
            f"You can only delete your own reviews!"
            )

    # If referer exists, redirect to it.
    # Otherwise, redirect to a default URL.
    if referer:
        return HttpResponseRedirect(referer)
    else:
        return HttpResponseRedirect('/')
        # Redirect to a default URL if no referer is found


# Define a view function to handle creating a video entry
def create_video(request):
    """
    View to render and submit a video creation form.
    """

    # Check if the request method is POST (i.e., form submission)
    if request.method == "POST":
        # Instantiate a video form with the POST data and files
        video_form = VideoForm(request.POST, request.FILES)

        # Validate the submitted video form
        if video_form.is_valid():
            # Save the video object without committing it to the database
            video = video_form.save(commit=False)
            # Assign the uploaded cover image to the video object
            video.cover = request.FILES.get('cover')
            # Save the video object to the database
            video.save()
            # Add a success message
            # indicating the successful addition of the video to the database
            messages.add_message(
                request, messages.SUCCESS, f"Video added to database."
                )
            # Clear the form for a new video entry
            video_form = VideoForm()
        else:
            # If the form is not valid, add an error message
            messages.add_message(
                request, messages.ERROR,
                f"Entry failed to submit. Please check form."
                )

    else:
        # If the request method is not POST, instantiate an empty video form
        video_form = VideoForm()

    # Create a context dictionary to pass data to the template
    context = {
        "video_form": video_form,
    }

    # Render the 'create_video.html' template with the context data
    return render(request, "videos/create_video.html", context)


# Define a view function to handle updating a video entry
def update_video(request, slug):
    """
    View to render and submit a video update form.
    """

    # Retrieve the video object with the provided slug from the database
    edit = get_object_or_404(Video, slug=slug)

    # Check if the request method is POST (i.e., form submission)
    if request.method == "POST":
        # Instantiate a video form with the POST data,
        # files, and the instance of the existing video
        video_form = VideoForm(request.POST, request.FILES, instance=edit)

        # Validate the submitted video form
        if video_form.is_valid():
            # Save the video object without committing it to the database
            video = video_form.save(commit=False)
            # Check if a new cover image is uploaded
            if request.FILES.get('cover'):
                # If a new cover image is uploaded,
                # assign it to the video object
                video.cover = request.FILES.get('cover')
            # Save the updated video object to the database
            video.save()
            # Add a success message
            # indicating the successful update of the video entry
            messages.add_message(
                request, messages.SUCCESS,
                f"Video entry updated."
                )
        else:
            # If the form is not valid, add an error message
            messages.add_message(
                request, messages.ERROR,
                f"Entry failed to submit. Please check form."
                )

    else:
        # If the request method is not POST,
        # instantiate a video form with the existing video instance
        video_form = VideoForm(instance=edit)

    # Create a context dictionary to pass data to the template
    context = {
        "video_form": video_form,
    }

    # Render the 'update_video.html' template with the context data
    return render(request, "videos/update_video.html", context)


class Page404(TemplateView):
    """
    Displays custom 404 page.
    """
    template_name = '404.html'


class Page500(TemplateView):
    """
    Displays custom 500 page.
    """
    template_name = '500.html'


class Page403(TemplateView):
    """
    Displays custom 403 page.
    """
    template_name = '403.html'