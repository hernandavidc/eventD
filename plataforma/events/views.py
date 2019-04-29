from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.mail import send_mail

from .forms import EventForm
from .models import Event, City, Invitation

@login_required
def createInvitation(request, pk):
    json_responder = {'created':False}
    if request.user.is_authenticated:
        event = Event.objects.get(pk=pk)
        invi = Invitation.objects.create(user=request.user, event=event)
        json_responder['created'] = True
        subject = 'You have a new invitation request'
        mailFrom = 'webmaster@localhost'
        mailTo = [request.user.email]
        content = request.user.username+" want to participate in your event please enter the platform and accept or decline your request."
        send_mail(subject, content,mailFrom,mailTo)
    else:
        raise Http404("The user is not authenticated.")
    return redirect(reverse_lazy('event_detail', args=[pk]))

@method_decorator(login_required, name="dispatch")
class EventCreate(CreateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('event_list')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})

@method_decorator(login_required, name="dispatch")
class EventUpdate(UpdateView):
    model = Event
    form_class = EventForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('event_update', args=[self.object.id]) + '?ok'

@method_decorator(login_required, name="dispatch")
class eventDetail(DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_anonymous:
            invi = self.object.get_requests.filter(user=self.request.user)
            if invi:
                context['invi'] = invi[0]
        return context

@method_decorator(login_required, name="dispatch")
class MyEventListView(TemplateView):
    template_name = 'events/myevent_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event_list'] =  self.request.user.get_pblshs.all()
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
            event_list = Event.objects.filter(user=request.user,name__contains=request.POST['name'], city = city, date=request.POST['date'])

        elif request.POST['name'] and request.POST['date']:
            contexto['name'] = request.POST['name']
            contexto['date'] = request.POST['date']
            event_list = Event.objects.filter(user=request.user,name__contains=request.POST['name'], date = request.POST['date'])

        elif request.POST['name'] and request.POST['city']:
            contexto['name'] = request.POST['name']
            contexto['cityId'] = request.POST['city']
            event_list = Event.objects.filter(user=request.user,name__contains=request.POST['name'], city = city)

        elif request.POST['city'] and request.POST['date']:
            contexto['cityId'] = int(request.POST['city'])
            contexto['date'] = request.POST['date']
            event_list = Event.objects.filter(user=request.user,city = city, date = request.POST['date'])

        elif request.POST['name']:
            contexto['name'] = request.POST['name']
            event_list = Event.objects.filter(user=request.user,name__contains=request.POST['name'])

        elif request.POST['date']:
            contexto['date'] = request.POST['date']
            event_list = Event.objects.filter(user=request.user,date=request.POST['date'])

        elif request.POST['city']:
            contexto['cityId'] = int(request.POST['city'])
            event_list = Event.objects.filter(user=request.user,city = city)

        else:
            event_list = ''
        
        contexto['event_list']=event_list
        return render(request, self.template_name, contexto)

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

@method_decorator(login_required, name="dispatch")
class InvitationListView(ListView):
    model = Invitation
    template_name = 'events/invitation_list.html'
    paginate_by = 30

    def get_queryset(self):
        if self.request.user.profile.notif:
            self.request.user.profile.notif = False
            self.request.user.profile.save()
        queryset = Invitation.objects.filter(event__user=self.request.user)
        return queryset

    def post(self, request, *args, **kwargs):
        cities = City.objects.all()
        contexto = {'cities':cities}

        if not(request.POST['event'] or request.POST['status']):
            return redirect('/requests/')
        
        if request.POST['event'] and request.POST['status']:
            contexto['eventId'] = request.POST['event']
            contexto['status'] = request.POST['status']
            if request.POST['status'] == '1':
                statusR = True
            elif request.POST['status'] == '0':
                statusR = False
            else:
                statusR = None
            invitation_list = Invitation.objects.filter(event__user=request.user,event__id=int(request.POST['event']), status=statusR)

        elif request.POST['event']:
            contexto['eventId'] = request.POST['event']
            invitation_list = Invitation.objects.filter(event__user=request.user,event__id=int(request.POST['event']))

        elif request.POST['status']:
            contexto['status'] = request.POST['status']
            if request.POST['status'] == '1':
                statusR = True
            elif request.POST['status'] == '0':
                statusR = False
            else:
                statusR = None
            invitation_list = Invitation.objects.filter(event__user=request.user,status=statusR)

        else:
            invitation_list = ''
        
        contexto['invitation_list']=invitation_list
        return render(request, self.template_name, contexto)

@method_decorator(login_required, name="dispatch")
class InvitationUpdateView(View):

    def get(self, request, *args, **kwargs):
        invi = Invitation.objects.get(id=kwargs['pk'])
        if kwargs['status'] == 'a':
            invi.status = True
            invi.save()
        elif kwargs['status'] == 'd':
            invi.status = False
            invi.save()
        return redirect(reverse_lazy('invitation_list'))