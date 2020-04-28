from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
class Event(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('calendarApp:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'