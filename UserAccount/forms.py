# -*- coding: utf-8 -*-
__author__ = 'hsn'

from django import forms
from django.contrib.auth.models import User
from UserAccount.models import Member

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),label='رمز عبور')
    first_name = forms.CharField(label='نام', max_length=100)
    last_name = forms.CharField(label='نام خانوادگی', max_length=100)
    username = forms.CharField(label='نام کاربری', max_length=100)
    email = forms.CharField(label='پست الکترونیکی', max_length=100)

    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password')

class MemberForm(forms.ModelForm):

    picture = forms.ImageField(label='عکس',required=False)
    tel = forms.CharField(label='تلفن',required=False)
    CHOICES=[('کارگر','کارگر'),('کارفرما','کارفرما')]

    m_type = forms.ChoiceField(label='ثبت نام به عنوان', choices=CHOICES, widget=forms.RadioSelect())


    class Meta:
        model = Member
        fields = ('picture','tel')

