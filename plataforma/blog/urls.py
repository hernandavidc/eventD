from django.urls import path
from . import views as blog_views
from .views import BlogDetailView

urlpatterns = [
    path('', blog_views.blog, name="blog"),
    path('<int:pk>/', BlogDetailView.as_view(), name='page'),
    path('categoria/<int:categoryId>/', blog_views.category, name="category"),
]