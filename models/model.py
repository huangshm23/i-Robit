from django.db import models


class Fund(models.Model):
    fundname = models.CharField(max_length=64, unique=True)
    fundno = models.CharField()
    profit = models.FloatField()


class Combination(models.Model):
    risk_factor = models.FloatField(primary_key=True)
    recommendation = models.CharField(max_length=1024)
    expected_rate = models.FloatField()
    std = models.FloatField()

