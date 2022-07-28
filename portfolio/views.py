from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all()  # GET ALL OBJECTS / not an error, Django support is not enabled in pycharm.
    return render(request, 'portfolio/home.html', {'projects': projects})
