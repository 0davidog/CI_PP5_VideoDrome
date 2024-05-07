from django import forms
from .models import Customer

class OrderForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
            'f_name',
            'l_name',
            'email',
            'phone',
            'street_address1',
            'street_address2',
            'town_or_city',
            'postcode',
            'county',
            'country',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'f_name': 'First Name',
            'l_name': 'Last Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'street_address1': 'Address Line 1',
            'street_address2': 'Address Line 2',
            'town_or_city': 'Town/City',
            'postcode': 'Postcode',
            'county': 'County',
        }

        self.fields['f_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
    