from django import forms
from .models import Customer

class CustomerInfoForm(forms.ModelForm):
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
            'name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'street_address1': 'Address Line 1',
            'street_address2': 'Address Line 2',
            'town_or_city': 'Town/City',
            'postcode': 'Postcode',
            'county': 'County',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
    