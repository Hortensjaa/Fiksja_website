import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from exclusivebooleanfield import ExclusiveBooleanField

from .categories import CATEGORIES


class Record(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(choices=CATEGORIES, max_length=50)
    description = models.TextField(blank=True, null=True, max_length=1000)

    def __str__(self):
        return self.title

    def current_break(self):
        return self.history.get(current_break=True)

    def has_a_break(self):
        return self.history.get(current_break=True)


class Break(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE, related_name='history')
    value = models.CharField(max_length=200, default='0')
    breaker = models.CharField(max_length=50)
    breaker_login = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True)
    break_date = models.DateField(default=timezone.now)
    break_place = models.CharField(default='Brzeg', blank=True, null=True, max_length=100)
    break_description = models.TextField(blank=True, null=True, max_length=1000)
    break_evidence = models.ImageField(blank=True, null=True)
    current_break = ExclusiveBooleanField(default=True, on=('record',))

    def __str__(self):
        return self.value
