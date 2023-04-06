from django.db import models
from datetime import datetime 
# Create your models here.
class Notice(models.Model):
    S_No=models.IntegerField(unique=True)
    title=models.CharField(max_length=100)
    message=models.TextField(max_length=500)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    