from django.contrib import admin
from user_dashboard.models import UserEvent

class UserEventAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_event', 'status')
        
admin.site.register(UserEvent, UserEventAdmin)
