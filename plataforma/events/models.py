from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField

# Create your models here.    
class City(models.Model):
    name = models.CharField(max_length=100,blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Cities"
    
    def __str__(self):
        return str(self.id) + " " + self.name
        
class Event(models.Model):
    user = models.ForeignKey(User, related_name="get_pblshs", on_delete=models.PROTECT)
    city = models.ForeignKey(City, related_name="get_events", on_delete=models.PROTECT)
    name = models.CharField(max_length=200,blank=False, null=False)
    description = RichTextField(null=True, blank=True)
    private = models.BooleanField(blank=False, null=False, default=False)
    date = models.DateField(blank=False, null=False)
    drctn = models.CharField(max_length=200,blank=False, null=False)
    image = models.ImageField(verbose_name="Imagen", upload_to="events", null=True, blank=True)
    cost =  models.PositiveSmallIntegerField(blank=True, null=True)
    urlMaps = models.URLField(max_length=500,blank=True, null=True)
    urlPay = models.URLField(max_length=500,blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = [ '-id']
    
    def __str__(self):
        return str(self.id) + " " + self.name + "-" + self.user.username

class Invitation(models.Model):
    user = models.ForeignKey(User, related_name="get_invitations", on_delete=models.PROTECT)
    event = models.ForeignKey(Event, related_name="get_requests", on_delete=models.PROTECT)
    status = models.BooleanField(default=None, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
