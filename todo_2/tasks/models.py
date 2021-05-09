from django.db import models

# Create your models here.
class Tasks(models.Model):
    text = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
