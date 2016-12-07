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

from moevmCommon.models.userProfile import UserProfile
from teacherPlan.forms import ScientificEventForm, AnotherWorkForm, QualificationForm, RemarkForm, RegisterTeacherForm
from .pdf.pdf_generate import conclusion_to_pdf
from moevmCommon.decorators import login_teacher_required

@login_teacher_required(login_url="/login")
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

@login_teacher_required(login_url="/login")
def logoutTeacher(request):
    logout(request)
    return HttpResponseRedirect('/login')

def registerTeacher(request):
    if request.method == 'POST':
        form = RegisterTeacherForm(request.POST)
        if form.is_valid():
            UserProfile.objects.create_teacher(
                username=request.POST['username'],
                email=request.POST['email'],
                password=request.POST['password'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                birth_date=request.POST['birth_date'],
                patronymic=request.POST['patronymic'],
                election_date=request.POST['election_date'],
                position=request.POST['position'],
                contract_date=request.POST['contract_date'],
                academic_degree=request.POST['academic_degree'],
                year_of_academic_degree=request.POST['year_of_academic_degree'],
                academic_status=request.POST['academic_status'],
                year_of_academic_status=request.POST['year_of_academic_status'],
                academic_state=request.POST['academic_state'],
                github_id=request.POST['github_id'],
                stepic_id=request.POST['stepic_id'],
            )
            return HttpResponseRedirect('/registerTeacher')
        return HttpResponseRedirect('/registerTeacher')

    else:
        return render(request, 'register_teacher.html',{'form':RegisterTeacherForm})



@login_teacher_required(login_url="/login")
def makeNewPlan(request):
    # todo реализовать логику
    return render(request, 'make_plan.html')

@login_teacher_required(login_url="/login")
def plan(request,id=1):
    # todo реализовать логику
    return render(request,'plan.html')

@login_teacher_required(login_url="/login")
def currentPlan(request):
    #todo реализовать логику
    return render(request,'plan.html')

@login_teacher_required(login_url="/login")
def listOfPlans(request):
    # todo реализовать логику
    return render(request, 'plan_list.html')

@login_teacher_required(login_url="/login")
def listOfPlans(request):
    # todo реализовать логику
    return render(request, 'plan_list.html')

@login_teacher_required(login_url="/login")
def makePDF(request,id=1):
    response = HttpResponse(content_type='application/pdf')
    somefilename = "somefilename" #TODO сделать нормальное имя для файла
    response['Content-Disposition'] = 'attachment; filename="' + somefilename + '.pdf"'

    return conclusion_to_pdf(response,id)

#forms
@login_teacher_required(login_url="/login")
def difWorkList(request, id=1):
    # todo реализовать логику
    return render(request, 'forms/dif_work_list.html',{'form':AnotherWorkForm})

@login_teacher_required(login_url="/login")
def disciplineList(request, id=1):
    # todo реализовать логику
    return render(request, 'forms/discipline_list.html',{'form':QualificationForm})

@login_teacher_required(login_url="/login")
def participationList(request, id=1):
    # todo реализовать логику
    return render(request, 'forms/participation_list.html',{'form':QualificationForm})

@login_teacher_required(login_url="/login")
def publicationList(request, id=1):
    # todo реализовать логику
    publications=1
    return render(request, 'forms/publication_list.html', {'form': ScientificEventForm})

@login_teacher_required(login_url="/login")
def qualificationList(request, id=1):
    # todo реализовать логику
    return render(request, 'forms/qualification_list.html',{'form':QualificationForm})

@login_teacher_required(login_url="/login")
def remarkList(request, id=1):
    # todo реализовать логику
    return render(request, 'forms/remark_list.html',{'form':RemarkForm})

@login_teacher_required(login_url="/login")
def scWorkList(request, id=1):
    # todo реализовать логику
    return render(request, 'forms/sc_work_list.html',{'form':QualificationForm})

@login_teacher_required(login_url="/login")
def studybookList(request, id=1):
    #todo реализовать логику
    return render(request, 'forms/studybook_list.html',{'form':QualificationForm})

# for managers

def managerReport(request):
    if request.user.is_superuser:
        return render(request,'manager/report.html')
    else:
        return HttpResponseRedirect("/login")
