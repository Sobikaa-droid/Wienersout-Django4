from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    #blogs_count = Blog.objects.order_by('-date')
    blogs = Blog.objects.order_by('-date')[:5]  # order by most recent ones // limit to 5 post per page
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)  # pk = primary key in database
    return render(request, 'blog/detail.html', {'id': blog_id, 'blog': blog})
