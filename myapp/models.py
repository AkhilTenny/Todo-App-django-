from django.db import models
import uuid


# Create your models here.


class TaskModel(models.Model):
  sino = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  task = models.CharField(max_length=255)
  date = models.CharField(max_length=32)
  done = models.BooleanField(default=False)
