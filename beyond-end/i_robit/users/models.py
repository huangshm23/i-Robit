from django.db import models

# Create your models here.

class User(models.Model):
    #gender_choice = [('male','男'),('female','女'),]
    username = models.TextField()
    password = models.TextField()
    is_active = models.BooleanField(default=False)
    #email = models.EmailField(unique=True)
    #gender = models.CharField(max_length=10,choices=gender_choice,default='男')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'

class Email_auth(models.Model):
    '''用于邮箱验证'''
    activate_id = models.CharField(max_length=8)
    email = models.CharField(max_length=32)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = '邮箱验证'
        verbose_name_plural = verbose_name
