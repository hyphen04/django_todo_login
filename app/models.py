from django.db import models


class Todo(models.Model):
    task = models.CharField(max_length=100)
    date = models.DateField()
