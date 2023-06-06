# Patterns for user app

from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # default authorized login
    path("",include('django.contrib.auth.urls')),

    # registration
    path("register/", views.register, name='register'),
]