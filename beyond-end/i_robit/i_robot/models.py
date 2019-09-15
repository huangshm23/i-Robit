from django.db import models

# Create your models here.

class News(models.Model):
    date = models.DateField()
    url = models.CharField(max_length=2083)
    title = models.CharField(max_length=255)
    time = models.DateTimeField()
    source = models.CharField(max_length=255)
    newspaper = models.TextField()

class Fund(models.Model):
    fundname = models.CharField(max_length=64, unique=True)
    fundno = models.CharField(max_length=24,null=True,blank=True)
    profit = models.FloatField()

    def __str__(self):
        return self.fundname


class Combination(models.Model):
    risk_factor = models.FloatField(primary_key=True)
    recommendation = models.CharField(max_length=1024)
    expected_rate = models.FloatField()
    std = models.FloatField()