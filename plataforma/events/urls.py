from django.urls import path
from .views import EventListView, eventDetail, createInvitation

urlpatterns = [
    path('events/', EventListView.as_view(), name='event_list'),
    path('event/<int:pk>/', eventDetail.as_view(), name='event_detail'),
    path('invi/<int:pk>/', createInvitation, name='invitation_create'),
]