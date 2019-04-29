from django.urls import path
from .views import ThreadList, ThreadDetail, add_message, start_thread

messenger_patterns = ([
    path('', ThreadList.as_view(), name='list'),
    path('<int:pk>/', ThreadDetail.as_view(), name='detail'),
    path('<int:pk>/add/', add_message, name='add'),
    path('start/<username>/', start_thread, name='start'),
], 'messenger')