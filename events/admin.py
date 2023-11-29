from django.contrib import admin
from events.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'time', 'location', 'slots', 'status')
        
admin.site.register(Event, EventAdmin)