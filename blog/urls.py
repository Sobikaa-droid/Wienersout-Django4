from django.urls import path
from . import views  # means import views from same folder where blog\urls is

app_name = 'blog'  # because of this stupid shit you have to do {% url 'blog:all_blogs' %} and not {% url 'all_blogs' %}

urlpatterns = [
    # this path below is 'localhost:8000/blog' because it set to 'blog/' in portfolio/views.py
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]
