from django import forms
from django.contrib.auth.models import User
from .models import Customer
class SavedAddressForm(forms.ModelForm):

    class Meta:
        model = Customer

        exclude = (
            'user',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'saved_street_address1': 'Address Line 1*',
            'saved_street_address2': 'Address Line 2',
            'saved_town_or_city': 'Town/City*',
            'saved_postcode': 'Postcode*',
            'saved_county': 'County',
            'saved_phone_number': 'Phone*',
        }

        for field in self.fields:
            if field != 'saved_country':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
    

class SavedDetailsForm(forms.ModelForm):

    class Meta:
        model = User

        fields = (
            'first_name', 
            'last_name',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }

        # iterate over fields to add matching placeholder and remove label
        for field in self.fields:
            # Set placeholder variable to matching field
            placeholder = placeholders[field]
            # Set placeholder attribute in form widget to our placeholder var value 
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # Remove existing field label
            self.fields[field].label = False
    
    def clean(self):
        cleaned_data = super().clean()
        # Iterate over fields and remove empty values
        for field_name, value in list(cleaned_data.items()):
            if value in [None, '']:
                del cleaned_data[field_name]
        return cleaned_data


