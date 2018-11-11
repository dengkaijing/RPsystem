# -*- coding: utf-8 -*-
#Author : dengkaijing

from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(required=True, max_length= 20)
    password = forms.CharField(required=True, min_length= 5)
    useremail = forms.EmailField(required=True)
