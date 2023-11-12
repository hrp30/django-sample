import datetime

from django.db import models


class Todo(models.Model):
    name = models.CharField(max_length=250, blank=True)
    description = models.TextField(max_length=300, blank=True)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
