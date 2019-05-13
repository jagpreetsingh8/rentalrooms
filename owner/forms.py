from django import forms
from owner.models import Owner
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput)
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email
        
    class Meta():
        model = User
        fields = ('username','password','password2','email')
    
    def __init__(self, *args, **kwargs):
        # remove any labels here if desired
        super(UserForm, self).__init__(*args, **kwargs)
        # remove the label of a non-linked/calculated field (txt01 added at top of form)
        self.fields['username'].widget = forms.TextInput(attrs={
            'name': 'username',
            'class': 'form-control'})
            
       # you can also remove labels of built-in model properties

        self.fields['password'].widget = forms.TextInput(attrs={
            'name': 'password',
            'class': 'form-control',})
        self.fields['password2'].widget = forms.TextInput(attrs={
            'name': 'password2',
            'class': 'form-control',})
        
        self.fields['email'].widget = forms.TextInput(attrs={
            'name': 'email',
            'class': 'form-control',})
       

class Reg_owner_form(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ('first_name','last_name','description','phone','photo')

    def __init__(self, *args, **kwargs):
        # remove any labels here if desired
        super(Reg_owner_form, self).__init__(*args, **kwargs)
        # remove the label of a non-linked/calculated field (txt01 added at top of form)
        self.fields['first_name'].widget = forms.TextInput(attrs={
            'class': 'form-control'})
            
       # you can also remove labels of built-in model properties

        self.fields['last_name'].widget = forms.TextInput(attrs={
            'class': 'form-control',})
        self.fields['description'].widget = forms.TextInput(attrs={
            'class': 'form-control',})
        self.fields['phone'].widget = forms.TextInput(attrs={
            'class': 'form-control',})
