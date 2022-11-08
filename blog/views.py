from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog

def index(request):
    blog = Blog.objects.all()
    context = {
        'blog': blog
    }
    return render (request, 'mainpage/index.html', context)
