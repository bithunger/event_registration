from django.db import models
from django.contrib.auth.models import User
from events.models import Event

class UserEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_event = models.ForeignKey(Event, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.user_event.title
    
