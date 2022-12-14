from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1, blank=True, null=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


