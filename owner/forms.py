from django import forms
from owner.models import Owner
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email
        
    class Meta():
        model = User
        fields = ('username','password','email')

class Reg_owner_form(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ('first_name','last_name','photo','description','phone')
