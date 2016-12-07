#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.auth import logout
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth

from teacherPlan.forms import ScientificEventForm, AnotherWorkForm, QualificationForm, RemarkForm
from .pdf.pdf_generate import conclusion_to_pdf

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
    # todo реализовать логику
    return render(request, 'make_plan.html')

@login_required(login_url="/login")
def plan(request,id=1):
    # todo реализовать логику
    return render(request,'plan.html')

@login_required(login_url="/login")
def currentPlan(request):
    #todo реализовать логику
    return render(request,'plan.html')

@login_required(login_url="/login")
def listOfPlans(request):
    # todo реализовать логику
    return render(request, 'plan_list.html')

@login_required(login_url="/login")
def listOfPlans(request):
    # todo реализовать логику
    return render(request, 'plan_list.html')

@login_required(login_url="/login")
def makePDF(request,id=1):
    response = HttpResponse(content_type='application/pdf')
    somefilename = "somefilename" #TODO сделать нормальное имя для файла
    response['Content-Disposition'] = 'attachment; filename="' + somefilename + '.pdf"'

    return conclusion_to_pdf(response,id)

#forms
@login_required(login_url="/login")
def difWorkList(request, id=1):
    # todo реализовать логику
    return render(request, 'forms/dif_work_list.html',{'form':AnotherWorkForm})

@login_required(login_url="/login")
def disciplineList(request, id=1):
    # todo реализовать логику
    return render(request, 'forms/discipline_list.html',{'form':QualificationForm})

@login_required(login_url="/login")
def participationList(request, id=1):
    # todo реализовать логику
    return render(request, 'forms/participation_list.html',{'form':QualificationForm})

@login_required(login_url="/login")
def publicationList(request, id=1):
    # todo реализовать логику
    publications=1
    return render(request, 'forms/publication_list.html', {'form': ScientificEventForm})

@login_required(login_url="/login")
def qualificationList(request, id=1):
    # todo реализовать логику
    return render(request, 'forms/qualification_list.html',{'form':QualificationForm})

@login_required(login_url="/login")
def remarkList(request, id=1):
    # todo реализовать логику
    return render(request, 'forms/remark_list.html',{'form':RemarkForm})

@login_required(login_url="/login")
def scWorkList(request, id=1):
    # todo реализовать логику
    return render(request, 'forms/sc_work_list.html',{'form':QualificationForm})

@login_required(login_url="/login")
def studybookList(request, id=1):
    #todo реализовать логику
    return render(request, 'forms/studybook_list.html',{'form':QualificationForm})

# for managers

def managerReport(request):
    if request.user.is_superuser:
        return render(request,'manager/report.html')
    else:
        return HttpResponseRedirect("/login")
