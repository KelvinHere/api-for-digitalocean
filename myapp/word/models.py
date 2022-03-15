from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=100)
    meaning = models.TextField(max_length=4096)

    def __str__(self):
        return self.word

class APICounter(models.Model):
    total_requests = models.IntegerField()

    def __str__(self):
        return self.total_requests