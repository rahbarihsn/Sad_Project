# -*- coding: utf-8 -*-
from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings
from django.template import RequestContext
from UserAccount.forms import UserForm,MemberForm,AddUserForm
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from UserAccount.models import Member,Employe,Master
from django.contrib.auth.models import User
# Create your views here.
def register(request):

    context = RequestContext(request)

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data= request.POST)
        member_form = MemberForm(data = request.POST)
        mem_type = request.POST.get('m_type')

        if user_form.is_valid() and member_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.is_active=False
            user.save()


            member = member_form.save(commit=False)
            member.user = user
            member.save()
            if mem_type == u'کارگر':
                member.member_type = 4
                member.save()
                employe = Employe.objects.create()
                employe.member = member
                employe.save()
            elif mem_type == u'کارفرما':
                member.member_type = 3
                member.save()
                master = Master.objects.create()
                master.member = member
                master.save()

            if 'picture' in request.FILES:
                member.picture = request.FILES['picture']


            registered = True
            send_mail('سامانه کاریاب', 'لطفا برای تایید ثبت نام خود بر روی لینک زیر کلیک بفرمایدی\nhttp://127.0.0.1:8000/register/activate_user/'+str(user.id), settings.EMAIL_HOST_USER, [user.email,],fail_silently=False)

        else:
            print user_form.errors, member_form.errors
    else:
        user_form = UserForm()
        member_form = MemberForm()

    return render(request,'register.html',
                          {'user_form':user_form, 'member_form':member_form , 'registered':registered})

def activate_user(request, id):
  user = User.objects.get(id=id)
  user.is_active=True
  user.save()
  return HttpResponse('activation_success_view')


def user_login(request):


    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                print user.username
                return HttpResponseRedirect('/user_account/'+str(user.username))
                # render(request,'user_account.html',{'member':Member.objects.get(user=user)})

            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request,'login.html',{})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponse('/main_page')



@login_required
def edit_profile(request):
    member = Member.objects.get(user=request.user)


    if request.method == 'GET':
        return render(request,'edit_profile.html',{'member':member})

    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        city = request.POST['city']
        town = request.POST['town']
        zone = request.POST['zone']
        region = request.POST['region']
        tel = request.POST['tel']
        # picture = request.FILES['picture']

        member.user.first_name = firstname
        member.user.last_name = lastname
        member.city = city
        member.zone = zone
        member.region = region
        member.tel = tel
        print firstname
        print city
        # member.picture = picture
        member.save()
        member.user.save()
        return HttpResponse("profile was updated")

@login_required
def show_order_work(request):
    member = Member.objects.get(user=request.user)
    return render(request,'order_work.html',{member})

def user_account(request,username):
    user = User.objects.get(username=username)
    member = Member.objects.get(user=user)
    return render(request,'user_account.html',{'member':member})

@login_required
def add_user(request):
    if request.method == 'POST':
        user_form = UserForm(data= request.POST)
        member_form = AddUserForm(data = request.POST)
        mem_type = member_form.member_type

        if user_form.is_valid() and member_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.is_active=False
            user.save()


            member = member_form.save(commit=False)
            member.user = user
            member.save()
            if mem_type == u'کارگر':
                member.member_type = 4
                member.save()
                employe = Employe.objects.create()
                employe.member = member
                employe.save()
            elif mem_type == u'کارفرما':
                member.member_type = 3
                member.save()
                master = Master.objects.create()
                master.member = member
                master.save()

            if 'picture' in request.FILES:
                member.picture = request.FILES['picture']


            registered = True

        else:
            print user_form.errors, member_form.errors
    else:
        user_form = UserForm()
        member_form = AddUserForm()

    return render(request,'register.html',
                          {'user_form':user_form, 'member_form':member_form , 'registered':registered})
