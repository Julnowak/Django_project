# DOCSTRING info
""" Definition of url patterns for learning_logs."""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    
    # Main page
    path('', views.index, name='index'),
]
