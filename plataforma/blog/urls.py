from django.urls import path
from . import views as blog_views

urlpatterns = [
    path('', blog_views.blog, name="blog"),
    path('categoria/<int:categoryId>/', blog_views.category, name="category"),
]