from django.db import models

# Create your models here.
# ORM notes 
# ORM = Object relational mapper 
# Makes a relationship between python and SQL so you can use your db in python

'''whenever we make changes here, we need to run python manage.py makemigrations & python manage.py migrate'''



class Project(models.Model):
    '''This is essentially us creating a database table. Project is the table name. We set up columns and info about it 
    so "title" is a column, and it has to be a character and max length of 100'''
    # CharField is VARCHAR
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    # We can put images in it! Put those paths in the static folder
    # image = models.FilePathField(path="projects/img")
    # this filepathfield command didn't work. Let's use a different one...
    #     WHEN YOU MAKE A CHANGE, MAKE MIGRATIONS CHANGES 
    image = models.CharField(max_length=100)

'''how do we load our db with data? 
run python manage.py shell
>>> from projects.models import Project
>>> p1 = Project(title = "test project", description="this is a test, 1234!", technology="Django", image="download.png")
>>> p1.save()

# you can query it too 

>>> results = Project.objects.all()
>>> results
<QuerySet [<Project: Project object (1)>]>
>>> p = results[0]
>>> p.title
'test project'
'''

'''what if we need to change data in the database after we migrate the data? (We could also just delete the database and make a new one)
>>> from projects.models import Project
>>> ps = Project.objects.all()
>>> p1 = ps[0]
>>> p2 = ps[1]
>>> p1.title
'test project'
>>> p1.image
'download.png'
>>> p1.image = 'projects/img/download.png'
>>> p1.save()
>>> p2.image = 'projects/img/download2.png'                                                                                                                                                                           
>>> p2.save()'''
