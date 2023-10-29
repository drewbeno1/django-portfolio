from django.shortcuts import render
# my code >
from django.http import HttpResponse
# import our db tables
from projects.models import Project

from projects.forms import ProjectForm
# Create your views here.
# My code here >>

# Need to return a Httpresponse:
#    What is that? an HttpResponse is the HTML that is the actual website. We can put it right here if we want to, but 
# def project_list(request):
#     return HttpResponse("<h1>Hello World!</h1>")
#    that isnt very clean, so instead we create an HTML template using render

# index.html is our template in templates/projects. We registered it and this view points to it now
# Why do we put projects within templates? in production, django combines all templates into one folder, so we need to 
#    specify which app goes with which template

def all_projects(request):
    # use this one to query the db to return all project objects
    '''VERY IMPORTTANT CONCEPT: The code in this function will run when the request tied to this function is called. 
    So in this instance, this prints whenever we navigate to the projects location .objects.all is the whole table '''
    projects = Project.objects.all()
    # print(projects)
    '''If you want it to show up on the screen, input a dictionary on the return statement, then we can render these objects in the html template '''
    return render(request, 'projects/all_projects.html', {'projects': projects})

'''Here is our project_detail which takes the request as an input'''
def project_detail(request, pk):
    # This is how the query gets pulled
    project = Project.objects.get(pk=pk)
    return render(request, 'projects/detail.html', {'project': project})
