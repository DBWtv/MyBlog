from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog

def index(request):
    blog = Blog.objects.all()
    context = {
        'blog': blog
    }
    print('blog:', blog)
    print('context:', context)
    return render (request, 'mainpage/index.html', context)
