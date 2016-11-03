# -*- coding: utf-8 -*-
from django.contrib.auth import logout
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth

@login_required(login_url="/login")
def index(request):
    return render(request,'index.html')


def loginTeacher(request):
    if request.method == 'POST':
        username = request.POST['loginField']
        password = request.POST['passwordField']
        print username
        print password
        user = auth.authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/loginwitherror')
        else:
            print "Некорректные данные: Логин {0}, Пароль {1}".format(username, password)
            return HttpResponseRedirect('/loginwitherror')
    return render(request, 'login.html')


def errorLoginTeacher(request):
    return render(request, 'login.html',{'error_message': 'Ошибка авторизации'})


@login_required(login_url="/login")
def logoutTeacher(request):
    logout(request)
    return HttpResponseRedirect('/login')


@login_required(login_url="/login")
def makeNewPlan(request):
    return render(request,'makeNewPlan.html')


@login_required(login_url="/login")
def plan(request):
    return render(request,'plan.html')


@login_required(login_url="/login")
def listOfPlans(request):
    return render(request,'listOfPlans.html')

# for managers

def managerReport(request):
    if request.user.is_superuser:
        return render(request,'manager/report.html')
    else:
        return HttpResponseRedirect("/login")
