from django.db import models
from django.utils import timezone

# Create your models here.


class Entry(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    high_priority = models.BooleanField(default=False)

    def __str__(self):
        return f"Title: {self.title}, High Priority: {self.high_priority}"

    class Meta:
        verbose_name_plural = "Entries"
