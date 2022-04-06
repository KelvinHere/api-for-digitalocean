from django.db import models
import datetime

class Word(models.Model):
    word = models.CharField(max_length=100)
    meaning = models.TextField(max_length=4096)
    edited = models.BooleanField(default=False)

    def __str__(self):
        return self.word

class APICounter(models.Model):
    requests = models.IntegerField(default=0)
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return str(self.requests)