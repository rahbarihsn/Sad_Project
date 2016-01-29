# -*- coding: utf-8 -*-
__author__ = 'hsn'

from django import forms
from django.contrib.auth.models import User
from UserAccount.models import Member


my_default_errors = {
    'required': 'لطفا این فیلد را پر نمایید',
    'invalid': 'لطفا یک مقدار مناسب وارد نمایید',
}
user_exist_errors = {
    'required': 'لطفا این فیلد را پر نمایید',
    'invalid': 'لطفا یک مقدار مناسب وارد نمایید',
    'unique':'کاربری با این نام وجود دارد'
}

class UserForm(forms.ModelForm):
    password = forms.CharField(error_messages=my_default_errors,widget=forms.PasswordInput(),label='رمز عبور')
    first_name = forms.CharField(error_messages=my_default_errors,label='نام', max_length=100)
    last_name = forms.CharField(error_messages=my_default_errors,label='نام خانوادگی', max_length=100)
    username = forms.CharField(error_messages=user_exist_errors,label='نام کاربری', max_length=100)
    email = forms.EmailField(error_messages=my_default_errors,label='پست الکترونیکی')

    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password')

class MemberForm(forms.ModelForm):

    picture = forms.ImageField(error_messages=my_default_errors,label='عکس',required=False)
    tel = forms.CharField(label='تلفن',required=False)
    CHOICES=[('کارگر','کارگر'),('کارفرما','کارفرما')]

    m_type = forms.ChoiceField(error_messages=my_default_errors,label='ثبت نام به عنوان', choices=CHOICES, widget=forms.RadioSelect())


    class Meta:
        model = Member
        fields = ('picture','tel')


class AddUserForm(forms.ModelForm):

    bankBalance = forms.IntegerField(error_messages=my_default_errors,label='موجودی حساب',required=False)
    picture = forms.ImageField(error_messages=my_default_errors,label='عکس',required=False)
    tel = forms.CharField(error_messages=my_default_errors,label='تلفن',max_length=20,required=False)
    city = forms.CharField(error_messages=my_default_errors,label='استان',max_length=20,required=False)
    town = forms.CharField(error_messages=my_default_errors,label='شهر',max_length=20,required=False)
    zone = forms.CharField(error_messages=my_default_errors,label='منطقه',max_length=20,required=False)
    region = forms.CharField(error_messages=my_default_errors,label='ناحیه',max_length=20,required=False)
    member_type = forms.IntegerField(error_messages=my_default_errors,label='نوع عضویت')

    class Meta:
        model = Member
        fields = ('bankBalance' ,'picture' , 'tel' , 'city' , 'town' , 'zone' , 'region', 'member_type' )




