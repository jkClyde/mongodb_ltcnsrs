from django.db import models

class CalendarEvent(models.Model):
    id = models.AutoField(primary_key=True)  # Add an 'id' field as the primary key
    title = models.CharField(max_length=255)
    date = models.DateField()
    isFinished = models.BooleanField(default=False)


