from django.shortcuts import render
from .models import Blog


def all_blogs(request):
    blogs = Blog.objects.order_by('-date')[:5]  # order by most recent ones // limit to 5 post per page
    return render(request, 'blog/all_blogs.html', {'blogs': blogs, 'blogs_num': len(blogs)})


def detail(request, blog_id):
    return render(request, 'blog/detail.html')
