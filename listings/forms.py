from django import forms
from listings.models import Listing


class listing_form(forms.ModelForm):
    class Meta:
        model = Listing
        fields = "__all__"

class add_listing(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('owner','title','address','city','state','zipcode','description','price','bedrooms','bathrooms','parking','food','security_fee','photo_main','photo_1','photo_2','photo_3','photo_4','photo_5','photo_6')

    def __init__(self, *args, **kwargs):
        # remove any labels here if desired
        super(add_listing, self).__init__(*args, **kwargs)
        # remove the label of a non-linked/calculated field (txt01 added at top of form)
        self.fields['title'].widget = forms.TextInput(attrs={
             'class' : 'form-control',
             'name': 'title'})
        self.fields['address'].widget = forms.TextInput(attrs={
            'class': 'form-control',})
        self.fields['city'].widget = forms.TextInput(attrs={
            'class': 'form-control',})
        self.fields['state'].widget = forms.TextInput(attrs={
            'class': 'form-control',})
        self.fields['zipcode'].widget = forms.TextInput(attrs={
            'class': 'form-control',})
        self.fields['description'].widget = forms.TextInput(attrs={
            'class': 'form-control',})
        # self.fields['price'].widget = forms.TextInput(attrs={
        #     'class': 'form-control',})
        # self.fields['bedrooms'].widget = forms.TextInput(attrs={
        #     'class': 'form-control',})
        # self.fields['bathrooms'].widget = forms.TextInput(attrs={
        #     'class': 'form-control',})
        # self.fields['parking'].widget = forms.TextInput(attrs={
        #     'class': 'form-control',})
        # self.fields['food'].widget = forms.TextInput(attrs={
        #     'class': 'form-control',})
        self.fields['security_fee'].widget = forms.TextInput(attrs={
            'class': 'form-control',})
        # self.fields['photo_main'].widget = forms.TextInput(attrs={
        #     'class': 'form-control',})
        # self.fields['photo_1'].widget = forms.TextInput(attrs={
        #     'class': 'form-control',})
        # self.fields['photo_2'].widget = forms.TextInput(attrs={
        #     'class': 'form-control',})
        # self.fields['photo_3'].widget = forms.TextInput(attrs={
        #     'class': 'form-control',})
        # self.fields['photo_4'].widget = forms.TextInput(attrs={
        #     'class': 'form-control',})
        # self.fields['photo_5'].widget = forms.TextInput(attrs={
        #     'class': 'form-control',})
        # self.fields['photo_6'].widget = forms.TextInput(attrs={
        #     'class': 'form-control',})
        # self.fields['list_date'].widget = forms.TextInput(attrs={
        #     'class': 'form-control',})
        



