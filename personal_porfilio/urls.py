"""personal_porfilio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.urls import path, include
from django.conf.urls.static import static  # here! if you come from the media root
from django.conf import settings  # after added media url in the settings we import it
from portfolio import views

# how to create a superuser to use the admin page
# go to the terminal and type in "python manage.py superuser" and fill out the things


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('blog/', include('blog.urls')),
]

# after we import the static we do this
# before this, you know the media root not media url 
# so to define media url, go back to the settings.py
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # once you've imported the settings, fill in the parenthesis like this