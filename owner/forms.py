from django import forms
from owner.models import Owner
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class Reg_owner_form(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ('first_name','last_name','photo','description','phone')
