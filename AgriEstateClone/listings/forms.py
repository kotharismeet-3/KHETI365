from django import forms
from .models import Listing


class ListingForm(forms.ModelForm):
    price = forms.DecimalField(max_digits=12, decimal_places=2)

    sqft = forms.DecimalField(max_digits=6, decimal_places=2)
    acre = forms.DecimalField(max_digits=4, decimal_places=2)

    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500)

    address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)
    zipcode = forms.CharField(max_length=20)

    photo_main = forms.ImageField()

    class Meta:
        model = Listing
        fields = ['price', 'sqft', 'acre', 'title', 'description', 'address', 'city', 'state',
                  'country', 'zipcode', 'photo_main']
