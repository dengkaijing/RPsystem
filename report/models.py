# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfileReporter(AbstractUser):
    nick_name = models.CharField(max_length=20, verbose_name="昵称", blank=True, null=True)
    user_creatDate = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '用户信息表'
        verbose_name_plural = verbose_name


# class UserProfileReceiver(models.Model):
#     nick_name = models.CharField(max_length=20, verbose_name="昵称", blank=True, null=True)
#     user_creatDate = models.DateTimeField(default=datetime.now)
#
#     class Meta:
#         verbose_name = '零等待用户信息表'
#         verbose_name_plural = verbose_name


class ReportedProblem(models.Model):
    recevier_name = models.CharField(max_length=20)
    receiver_email = models.CharField(max_length=20)
    device_ip = models.CharField(max_length=20)
    device_version = models.CharField(max_length=20)
    problem_text = models.CharField(max_length=200)

    class Meta:
        verbose_name = '问题单详情表'
        verbose_name_plural = verbose_name

class Devices(models.Model):
    IP_Number = models.GenericIPAddressField(verbose_name="设备IP")
    source_choice = ( (0,"ARM"),
                      (1,"Dorado5000"),
                      (2,"Dorado6000"),
    )
    Device_version = models.SmallIntegerField(choices=source_choice,verbose_name="设备版本")

    class Meta:
        verbose_name = '设备表'
        verbose_name_plural = verbose_name