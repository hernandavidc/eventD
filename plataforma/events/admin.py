from django.contrib import admin
from .models import Event, Invitation, City

class EventAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')
    ordering = ('-created',)
    search_fields = ('user', 'city', 'name')
    list_filter = ('user', 'city')

class CityAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')
    ordering = ('created',)
    search_fields = ('nombre',)

admin.site.register(Invitation)
admin.site.register(Event, EventAdmin)
admin.site.register(City, CityAdmin)
