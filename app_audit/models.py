from django.db import models

class Audit(models.Model):
    time_created = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=255)
    action = models.CharField(max_length=255)

    @property
    def formatted_time_created(self):
        return str(self.time_created)

    def __str__(self):
        return f"{self.user} - {self.action} ({self.formatted_time_created})"
