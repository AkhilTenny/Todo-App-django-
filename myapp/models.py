from django.db import models

# Create your models here.


class TaskModel(models.Model):
  task = models.CharField(max_length=255)
  date = models.CharField(max_length=32)
