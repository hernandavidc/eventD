from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def blog(request):
    template_name = 'blog/blog.html'
    posts = Post.objects.all()
    contexto = {'posts':posts}
    return render(request, template_name, contexto)

def category(request, categoryId):
    template_name = 'blog/category.html'
    category = get_object_or_404(Category, id=categoryId)
    contexto = {'category':category}
    return render(request, template_name, contexto)
