from django import forms
from listings.models import Listing


class listing_form(forms.ModelForm):
    class Meta:
        model = Listing
        fields = "__all__"
