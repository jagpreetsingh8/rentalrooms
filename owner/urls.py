from django.urls import path
from . import views

app_name = 'owner'

urlpatterns = [
      path('owner_register', views.register, name = 'register'),
  
]