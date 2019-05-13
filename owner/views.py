from django.shortcuts import render,redirect
from owner.forms import UserForm,Reg_owner_form
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages,auth
from django.contrib.auth.models import User

def register(request):
    #registered = False
    if request.method == 'POST':

         # Get form values
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2'] 

        #check if passwords match
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'that username is taken')
                return redirect('owner:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'that email is taken')
                    return redirect('owner:register')
                else:
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
            messages.error(request, 'Password do not match')
            return redirect('owner:register')
   
    else:
        user_form = UserForm()
        profile_form = Reg_owner_form()
    return render(request,'owner/register.html',
                          {'user_form':user_form,
                           'profile_form':profile_form})
                    
                    # user = User.objects.create_user(username=username,password=password,
                    # email=email,first_name=first_name,last_name=last_name)
                    # #login after register
                    # # auth.login(request, user)
                    # # messages.success(request, 'you are now logged in')
                    # # return redirect('index')
                    # user.save()
                    # messages.success(request, 'you are now registered and can log in')
                    # return redirect('login')
                    # # end of nested if
     
        
   


    #     user_form = UserForm(data=request.POST)
    #     profile_form = Reg_owner_form(data=request.POST)
    #     if user_form.is_valid() and profile_form.is_valid():
    #         user = user_form.save()
    #         user.set_password(user.password)
    #         user.save()
    #         profile = profile_form.save(commit=False)
    #         profile.user = user
    #         if 'photo' in request.FILES:
    #             print('found it')
    #             profile.photo = request.FILES['photo']
    #         profile.save()
    #         return redirect('login')
    #        # registered = True
    #     else:
    #         print(user_form.errors,profile_form.errors)
    # else:
    #     user_form = UserForm()
    #     profile_form = Reg_owner_form()
    # return render(request,'owner/register.html',
    #                       {'user_form':user_form,
    #                        'profile_form':profile_form})

