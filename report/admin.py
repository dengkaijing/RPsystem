# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from report import models
# Register your models here.

#admin.site.register(models.UserProfileReporter)

admin.site.register(models.ReportedProblem)
admin.site.register(models.Devices)
admin.site.register(models.UserProfileReporter)