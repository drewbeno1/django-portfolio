from django.forms import ModelForm
from projects.models import Project
'''This is how you do a data entry form
Also add in steps to views and the html
This isn't quite working'''
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
