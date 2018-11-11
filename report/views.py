# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from django.contrib.auth.backends.ModelBackend
from django.shortcuts import render, redirect, HttpResponseRedirect

from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.views.generic.base import View
from django.core.urlresolvers import reverse
from reportfroms import RegisterForm
from django.contrib.auth.hashers import make_password
import models


# Create your views here.


class UserLogin(View):
    def get(self, request):
        return render(request, "loginuser.html")

    def post(self, request):
        user_name = request.POST.get("username", "")
        user_password = request.POST.get("password", "")
        usr = authenticate(username=user_name, password=user_password)
        if usr is not None:
            login(request, usr)
            return HttpResponseRedirect(reverse("submitreport"))

            # return render(request, "ioio.html")
        # {"value": usr.is_authenticated.value,
        #                                        "email": usr.email,
        #                                        "username": usr.username}

        else:
            return render(request, "loginuser.html")


class SubmitReport(View):
    def get(self, request):
        return render(request, "ioio.html")

    def post(self, request):
        recevier_name = request.user.username
        receiver_email = request.POST.get("recevier")
        device_ip = request.POST.get("device_ip")
        device_version = request.POST.get("device_version")
        problem_text = request.POST.get("problem_text")
        #        print (request.session.session_key)

        send_mail(device_ip + u"故障，需要及时修复,版本是：" + device_version,
                  problem_text,
                  request.user.email,
                  [receiver_email, ], fail_silently=False)

        report_problem = models.ReportedProblem()
        report_problem.recevier_name = recevier_name
        report_problem.receiver_email = receiver_email
        report_problem.device_ip = device_ip
        report_problem.device_version = device_version
        report_problem.problem_text = problem_text
        report_problem.save()

        return render(request, "ioio.html")


class RegisterView(View):
    def get(self, request):
        registerform = RegisterForm()
        return render(request, "register.html", {"registerform": registerform})

    def post(self, request):
        registerform = RegisterForm(request.POST)
        if registerform.is_valid():
            user_name = request.POST.get("username")
            if models.UserProfileReporter.objects.filter(username=user_name):
                return render(request, reverse("registeruser"), {"msg": "此用户名已经存在"})
            user_password = request.POST.get("password")
            user_email = request.POST.get("useremail")
            userprofilereporter = models.UserProfileReporter()
            userprofilereporter.username = user_name
            userprofilereporter.password = make_password(user_password)
            userprofilereporter.email = user_email
            userprofilereporter.save()
            return HttpResponseRedirect(reverse("loginuser"))
