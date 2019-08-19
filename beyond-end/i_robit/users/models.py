from django.db import models

# Create your models here.
'''
class User(models.Model):
    gender_choice = [('male','男'),('female','女'),]
    username = models.CharField(max_length=64,unique=True)
    password = models.CharField(max_length=12)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10,choices=gender_choice,default='男')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'
'''