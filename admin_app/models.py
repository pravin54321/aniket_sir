from django.db import models
class PyamentStatusModel(models.Model):
    Device_id=models.CharField(max_length=200)
    Status=models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation Date")

# Create your models here.
