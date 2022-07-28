from django.urls import path
from . import views  # means import views from same folder where blog\urls is

urlpatterns = [
    # this path below is 'localhost:8000/blog' because it set to 'blog/' in portfolio/views.py
    path('', views.all_blogs, name='all_blogs'),
]
