from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)


class HostInfo(models.Model):
    hostname = models.CharField(max_length=32)
    task = models.CharField(max_length=32)
    user_info = models.ForeignKey("UserInfo", to_field='id')
