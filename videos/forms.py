from django import forms
from django.forms.widgets import TextInput
from .models import UserReview, Video, Genre, Language, Subtitle

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


class VideoForm(forms.ModelForm):
    """
    """

    class Meta:
        model = Video
        fields = {
            'title', 
            'director', 
            'format', 
            'discs',
            'condition',
            'price',
            'stock',
            'cover',
            'overview',
            'overview_source',
            'trailer', 
            'release_year', 
            'certificate',
            'aspect_ratio', 
            'feature_length',
            'on_sale', 
            'languages', 
            'subtitles',
            'region', 
            'genre', 
        }
        widgets = {
            "release_year": TextInput(),
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Video Title', 
            'director': 'Video Director', 
            'format': 'Video Format', 
            'discs': 'Number of Discs', 
            'condition': 'Video Condition',
            'price': 'Video Price',
            'stock': 'Units in Stock',
            'cover': 'Cover Image',
            'overview': 'Video Overview',
            'overview_source': 'Wikipedia URL',
            'trailer': 'YouTube Trailer URL', 
            'release_year': 'Original Release Year', 
            'certificate': 'Certificate/Age Rating',
            'aspect_ratio': 'Video Aspect Ratio', 
            'feature_length': 'Length of Main Feature',  
            'on_sale': 'Available For Sale', 
            'languages': 'Available Langauges', 
            'subtitles': 'Available Subtitles',
            'region': 'Video Region Code', 
            'genre': 'Video Genre', 
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            
            self.fields[field].widget.attrs['placeholder'] = placeholder
            
            self.fields[field].label = False


class GenreForm(forms.ModelForm):
    """
    """
    class Meta:
        model = Genre

        fields= {
            'genre_name',
        }

        labels = {
            'genre_name': 'Add a new Genre Name:',
        }


class LanguageForm(forms.ModelForm):
    """
    """
    class Meta:
        model = Language

        fields= {
            'language',
        }

        labels = {
            'language': 'Add a new Language Track:',
        }



class SubtitleForm(forms.ModelForm):
    """
    """
    class Meta:
        model = Subtitle

        fields= {
            'subtitle',
        }

        labels = {
            'subtitle': 'Add a new subtitle Track:',
        }

