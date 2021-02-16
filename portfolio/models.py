from django.db import models

class Project(models.Model):  # modeling the table that goes into the database
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)  # blank=True allows you to not set the url

    def __str__(self):
        return self.title


# how to add a modeling class to my database
# 1. go to the terminal
# - it says i have unapplied migrations 
# - anytime i make a change or something new with your models, it's called a migration
# - and those things need to be migrated into the database
# - basically migrating means me telling the database there's a new table or changes about a table
# - as soon as you make a model, "python manage.py migrations"
# - and then migrate it


# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX #
# 2. type in the terminal "python manage.py migrate"
# 3. after that in order for the system to know about it, type in "python manage.py makemigrations" / it sounds like adding and committing in git 
# - makemigrations check any of my models.py files and see if there are new changes there. it says "create model 'classname'"
# and then run the server again and it says i have one unapplied migration again
# 4. then type in "python manage.py migrate" again after it's done i get no migration messages
# now you have migration file in the migrations folder. 
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX #

# how to change a model
# change a property of the model
# and go to terminal
# and type in "python manage.py makemigrations"
# then you're gonna have a new migration python file in the migration folder 
# if you wanna cancel the changes just delete the file