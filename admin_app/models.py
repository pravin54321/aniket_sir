from django.db import models
class PyamentStatusModel(models.Model):
    Device_id=models.CharField(max_length=200)
    Status=models.CharField(max_length=200)

# Create your models here.
