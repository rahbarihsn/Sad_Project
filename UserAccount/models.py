from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

import datetime

# Create your models here.
# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(User,default=0)
    bankBalance = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='profile_images',blank=True)
    tel = models.CharField(blank=True,max_length=20)
    city = models.CharField(blank=True,max_length=20)
    town = models.CharField(blank=True,max_length=20)
    zone = models.CharField(blank=True,max_length=20)
    region = models.CharField(blank=True,max_length=20)
    member_type = models.IntegerField(blank=False,default=0)
    def __unicode__(self):
        return self.user.username


class Master(models.Model):
    member = models.OneToOneField(Member,default=0)
    rate = models.FloatField(default=0)
    def __unicode__(self):
        return self.member.user.username

class Employe(models.Model):
    member = models.OneToOneField(Member,default=0)
    rate = models.FloatField(default=0)
    def __unicode__(self):
        return self.member.user.username

class Profession(models.Model):
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name

class Emp_prfn(models.Model):
    class Meta:
        unique_together = (('employe', 'prfn'),)
    employe = models.ForeignKey(Employe)
    prfn = models.ForeignKey(Profession)
    price = models.IntegerField(default=0)
    def __unicode__(self):
        return self.employe + self.prfn.name

class Task(models.Model):
    emp_prfn_rel = models.ForeignKey(Emp_prfn)
    master = models.ForeignKey(Master)
    date = models.DateField()
    status = models.CharField(max_length=10)

class Task_employe(models.Model):
    task = models.ForeignKey(Task)
    employe = models.ForeignKey(Employe)

class Transaction(models.Model):
    price = models.IntegerField(default=0)
    date = models.DateField(default=datetime.datetime.now)
    master = models.ForeignKey(Master)
    employe = models.ForeignKey(Employe)
    def __unicode__(self):
        return self.member.user.username

