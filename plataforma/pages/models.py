from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")

    class Meta:
        verbose_name_plural = "categories"
        ordering = ['-created']

    def __str__(self):
        return self.name

class Page(models.Model):
    title = models.CharField(verbose_name="Title", max_length=200)
    content = RichTextField(verbose_name="Content", config_name = 'default')
    order = models.SmallIntegerField(verbose_name="Order", default=0)
    published = models.DateTimeField(verbose_name="Publisehd", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Author", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categories", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Update")

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
        ordering = ['-order', '-id', 'title']

    def __str__(self):
        return self.title
