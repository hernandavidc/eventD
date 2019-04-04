from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Event, City, Invitation

@login_required
def createInvitation(request, pk):
    json_responder = {'created':False}
    if request.user.is_authenticated:
        event = Event.objects.get(pk=pk)
        invi = Invitation.objects.create(user=request.user, event=event)
        json_responder['created'] = True
    else:
        raise Http404("El usuario no esta autenticado")
    return redirect(reverse_lazy('event_detail', args=[pk]))


class eventDetail(DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_anonymous:
            invi = self.object.get_requests.filter(user=self.request.user)
            if invi:
                context['invi'] = invi[0]
        return context

class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = City.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        cities = City.objects.all()
        contexto = {'cities':cities}

        if not(request.POST['name'] or request.POST['city'] or request.POST['date']):
            return redirect('/events/')
        
        if request.POST['city']:
            city = int(request.POST['city'])

        if request.POST['city'] and request.POST['name'] and request.POST['date']:
            contexto['name'] = request.POST['name']
            contexto['cityId'] = int(request.POST['city'])
            contexto['date'] = request.POST['date']
            event_list = Event.objects.filter(name__contains=request.POST['name'], city = city, date=request.POST['date'])

        elif request.POST['name'] and request.POST['date']:
            contexto['name'] = request.POST['name']
            contexto['date'] = request.POST['date']
            event_list = Event.objects.filter(name__contains=request.POST['name'], date = request.POST['date'])

        elif request.POST['name'] and request.POST['city']:
            contexto['name'] = request.POST['name']
            contexto['cityId'] = request.POST['city']
            event_list = Event.objects.filter(name__contains=request.POST['name'], city = city)

        elif request.POST['city'] and request.POST['date']:
            contexto['cityId'] = int(request.POST['city'])
            contexto['date'] = request.POST['date']
            event_list = Event.objects.filter( city = city, date = request.POST['date'])

        elif request.POST['name']:
            contexto['name'] = request.POST['name']
            event_list = Event.objects.filter(name__contains=request.POST['name'])

        elif request.POST['date']:
            contexto['date'] = request.POST['date']
            event_list = Event.objects.filter(date=request.POST['date'])

        elif request.POST['city']:
            contexto['cityId'] = int(request.POST['city'])
            event_list = Event.objects.filter( city = city)

        else:
            event_list = ''
        
        contexto['event_list']=event_list
        return render(request, self.template_name, contexto)
