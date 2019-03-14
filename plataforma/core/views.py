from django.views.generic import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):


    contexto = {'title':"Events"}
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)

#class SampleView(TemplateView):
#    template_name = "core/sample.html"

