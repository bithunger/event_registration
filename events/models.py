from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.CharField(max_length=30)
    location = models.CharField(max_length=200)
    slots = models.IntegerField()
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
