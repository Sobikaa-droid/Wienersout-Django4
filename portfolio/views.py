from django.shortcuts import render
from .models import Project


def home(request):
    Project.objects()  # this is not an error, my Django support is not enabled in pycharm.
    return render(request, 'portfolio/home.html')
