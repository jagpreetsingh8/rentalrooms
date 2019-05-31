from django import forms
from listings.models import Listing
from owner.models import Owner


class listing_form(forms.ModelForm):
    class Meta:
        model = Listing
        fields = "__all__"

class add_listing(forms.ModelForm):
   # owner = forms.ModelChoiceField(queryset=Owner.objects.all(),widget=forms.HiddenInput())
    class Meta:
        model = Listing
        fields = ('owner','title','address','city','state','zipcode','description','price','bedrooms','bathrooms','parking','food','security_fee','photo_main','photo_1','photo_2','photo_3','photo_4','photo_5','photo_6')
        exclude = ['owner',]
        labels = {
            "parking": "Gender"
        }
        #fields = "__all__"

    def clean_city(self):
        city = self.cleaned_data['city']
        
        if city:
            if not city.isalpha():
                raise forms.ValidationError("City  should be alphabetic")
        return city
    
    def clean_state(self):
        state = self.cleaned_data['state']
        
        if state:
            if not state.isalpha():
                raise forms.ValidationError("State name should be alphabetic")
        return state
    
    def clean_zipcode(self):
        zipcode = self.cleaned_data['zipcode']
        
        if zipcode:
            if not zipcode.isdigit():
                raise forms.ValidationError("Zipcode name should be Numeric")
        return zipcode

    def clean_security_fee(self):
        security_fee = self.cleaned_data['security_fee']
        
        if security_fee:
            if not security_fee.isdigit():
                raise forms.ValidationError("Security Fee name should be Numeric")
        return security_fee
        

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
        self.fields['price'].widget = forms.TextInput(attrs={
            'class': 'form-control',})
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
    


