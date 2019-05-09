from django.shortcuts import render,redirect
from owner.forms import UserForm,Reg_owner_form
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def register(request):
    #registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = Reg_owner_form(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'photo' in request.FILES:
                print('found it')
                profile.photo = request.FILES['photo']
            profile.save()
            return redirect('login')
           # registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = Reg_owner_form()
    return render(request,'owner/register.html',
                          {'user_form':user_form,
                           'profile_form':profile_form})

