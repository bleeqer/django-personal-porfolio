from django.urls import path
from . import views

# how to create a superuser to use the admin page
# go to the terminal and type in "python manage.py superuser" and fill out the things



urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    
    ]
