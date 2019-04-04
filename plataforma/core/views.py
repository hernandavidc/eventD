from django.views.generic import TemplateView
from django.shortcuts import render

from blog.models import Post
from events.models import Event

class HomePageView(TemplateView):
    posts = Post.objects.all()[:5]
    events = Event.objects.all()[:6]

    contexto = {'title':"Events", 'posts':posts, 'events':events}
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)

#class SampleView(TemplateView):
#    template_name = "core/sample.html"

