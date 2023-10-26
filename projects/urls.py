from django.urls import path
from projects import views

# We create this one so that it know when it gets redirected to '', push forward to projects views.py
# this path adds another path. so now we need website/projects/test for it to work
urlpatterns = [
    path('', views.all_projects),
    path('test', views.project_list)
]