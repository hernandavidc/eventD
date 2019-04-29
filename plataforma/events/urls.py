from django.urls import path
from .views import InvitationUpdateView, InvitationListView, EventUpdate, MyEventListView, EventListView, eventDetail, createInvitation, EventCreate

urlpatterns = [
    path('events/', EventListView.as_view(), name='event_list'),
    path('my-events/', MyEventListView.as_view(), name='myevent_list'),
    path('event/update/<int:pk>/', EventUpdate.as_view(), name='event_update'),
    path('event/<int:pk>/', eventDetail.as_view(), name='event_detail'),
    path('event/add/', EventCreate.as_view(), name='event_add'),
    path('invi/<int:pk>/', createInvitation, name='invitation_create'),
    path('invi/<str:status>/<int:pk>/', InvitationUpdateView.as_view(), name='invitation_update'),
    path('requests/', InvitationListView.as_view(), name='invitation_list'),
]