from django.shortcuts import render
from .models import Project  # import a model

# making an url 
# go to urls.py declare a path, view, name
# come here define a function with a template that you're gonna use
# create a html file in the portfolio folder like portfolio/templates/portfolio/name.html

# this is where you grab a table/model from the database and put it into a view to display the table/model objects

def home(request):
    projects = Project.objects.all()  # so you made a class(Project) and it brings all the objects you've created with the class
    return render(request, 'portfolio/home.html', {'projects':projects})