from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Post, Category

def blog(request):
    template_name = 'blog/blog.html'
    categories = Category.objects.all()
    posts = Post.objects.all()
    contexto = {'posts':posts, 'categories':categories}
    return render(request, template_name, contexto)

def category(request, categoryId):
    template_name = 'blog/category.html'
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=categoryId)
    contexto = {'category':category, 'categories':categories}
    return render(request, template_name, contexto)

class BlogDetailView(DetailView):
    model = Post
