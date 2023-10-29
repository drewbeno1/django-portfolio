from django.urls import path
from projects import views

# name our app_name the same as our app that we are
app_name = 'projects'

# We create this one so that it know when it gets redirected to '', push forward to projects views.py
# this path adds another path. so now we need website/projects/test for it to work
'''The names allow us to uniquely identify the view URL's we point to '''
urlpatterns = [
    path('', views.all_projects, name="all_projects"),
    # this syntax captures just one part of the path and passes it forward based on the selected variable
    #   in this instance that variable is pk
    #   int = integer path converter. It ensures that the inserted pk is a number, then goes to project_detail view with the submitted integer
    # ### ALSO, the path here is going to be the pk at the end of the last path. so for example, would be /1
    # ### If its not a valid pk then it won't do anything. 
    path('<int:pk>', views.project_detail, name="project_details")
]