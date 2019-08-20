from django.db import models

# Create your models here.

class News(models.Model):
    date = models.DateField()
    url = models.CharField(max_length=2083)
    title = models.CharField(max_length=255)
    time = models.DateTimeField()
    source = models.CharField(max_length=255)
    newspaper = models.TextField()
