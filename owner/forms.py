from django import forms
from owner.models import Owner
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email
        
    class Meta():
        model = User
        fields = ('username','password','password2','email')
        labels = {
            "password2": "Confirm Password"
        }

    def clean_password2(self):
        pas = self.cleaned_data['password']
        cpas = self.cleaned_data['password2']
        MIN_LENGTH = 8
        if pas and cpas:
            if len(pas) < MIN_LENGTH:
                raise forms.ValidationError("password should have at least %d character" %MIN_LENGTH)
            if pas.isdigit():
                raise forms.ValidationError("password should not all numeric")

    
    
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
        self.fields['email'].required=True
       

class Reg_owner_form(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ('first_name','last_name','description','phone','photo')

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        
        if first_name:
            if not first_name.isalpha():
                raise forms.ValidationError("First name should be alphabetic")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        
        if last_name:
            if not last_name.isalpha():
                raise forms.ValidationError("Last name should be alphabetic")
        return last_name

    

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
        self.fields['phone'].required=True

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        MIN_LENGTH = 10
        if phone:
            if len(phone) < MIN_LENGTH:
                raise forms.ValidationError("Phone should have at least %d character" %MIN_LENGTH)
            if not phone.isdigit():
                raise forms.ValidationError("Phone should all numeric")
        return phone
