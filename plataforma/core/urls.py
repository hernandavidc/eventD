from django.urls import path
from .views import HomePageView #, SampleView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    #path('sample/', SampleView.as_view(), name="sample"),
]