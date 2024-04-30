from django import forms
from .models import UserReview

class ReviewForm(forms.ModelForm):
    """
    Form for adding a review on a video detail page.
    Related to :model: `UserReview`
    """
    class Meta:
        model = UserReview
        fields = ('title', 'content',)
        labels = {
            "title": "Review Title:",
            "content": "Your Review:",
        }