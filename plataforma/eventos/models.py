from django.db import models
from django.contrib.auth.models import User

# Create your models here.    
class City(models.Model):
    name = models.CharField(max_length=100,blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.id) + " " + self.name
        
class Event(models.Model):
    user = models.ForeignKey(User, related_name="get_pblshs", on_delete=models.PROTECT)
    city = models.ForeignKey(City, related_name="get_events", on_delete=models.PROTECT)
    name = models.CharField(max_length=200,blank=False, null=False)
    descripcion = models.TextField(null=True, blank=True)
    date = models.DateField(blank=False, null=False)
    urlMaps = models.URLField(max_length=200,blank=True, null=True)
    urlPay = models.URLField(max_length=200,blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Invitation(models.Model):
    user = models.ForeignKey(User, related_name="get_invitations", on_delete=models.PROTECT)
    event = models.ForeignKey(Event, related_name="get_requests", on_delete=models.PROTECT)
    status = models.BooleanField(default=None, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
