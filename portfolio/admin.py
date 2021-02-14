from django.contrib import admin
from .models import Project  # importing the model we wanna have here
# you have to specify what models you wnat to show up inside of that admin on the page

admin.site.register(Project)  # do this if you want the model to be inside of the admin page. this is all it takes
                              # once you register the model you can add, edit or delete a Project
                              # but, remember you added image and the directory that doesn't exist to the model?
                              # when you upload an image it's gonna be saved in the directory you defined in the model
                              # but we need cleaner way to do that, go to at the end of the code in the settings.py 
                        

