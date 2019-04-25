from django.urls import path
from . import views

app_name = 'owner'

urlpatterns = [
      path('register', views.register, name = 'register'),
  
]