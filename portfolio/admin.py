from django.contrib import admin
from .models import Project  # models.py import Project class

admin.site.register(Project)  # what models to appear inside of the admin
