#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.auth import logout
from django.http import Http404
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth
import datetime
from moevmCommon.models import UserProfile
from teacherPlan.forms import *
from .pdf.pdf_generate import conclusion_to_pdf
from moevmCommon.decorators import login_teacher_required

@login_teacher_required(login_url="/teacherPlan/login")
def index(request):
    return render(request, 'teacherPlan/index.html')

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
                return HttpResponseRedirect('/teacherPlan/')
            else:
                return HttpResponseRedirect('/teacherPlan/loginwitherror')
        else:
            print "Некорректные данные: Логин {0}, Пароль {1}".format(username, password)
            return HttpResponseRedirect('/loginwitherror')
    return render(request, 'teacherPlan/login.html')

def errorLoginTeacher(request):
    return render(request, 'teacherPlan/login.html', {'error_message': 'Ошибка авторизации'})

@login_required(login_url="/teacherPlan/login")
def logoutTeacher(request):
    logout(request)
    return HttpResponseRedirect('/teacherPlan/login')

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
        return render(request, 'teacherPlan/register_teacher.html', {'form':RegisterTeacherForm})



@login_teacher_required(login_url="/teacherPlan/login")
def plan(request,id=1):
    try:
        tp = TeacherPlan.objects.get(id=id)
    except:
        raise Http404
    return render(request, 'teacherPlan/plan.html',{'plan': tp, 'user_profile': tp.person_profile})

@login_teacher_required(login_url="/teacherPlan/login")
def currentPlan(request):
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    user_profile = UserProfile.get_profile_by_user(request.user)
    plan=None
    if month < 8:
        plan = TeacherPlan.objects.get_or_create(person_profile = user_profile, start_year = (year - 1))[0]
    else :
        plan = TeacherPlan.objects.get_or_create(person_profile = user_profile, start_year = year)[0]
    return render(request, 'teacherPlan/plan.html',{'plan':plan,'user_profile':user_profile})

@login_teacher_required(login_url="/teacherPlan/login")
def listOfPlans(request):
    up = UserProfile.get_profile_by_user(request.user)
    list = TeacherPlan.objects.all().filter(person_profile=up)
    return render(request, 'teacherPlan/plan_list.html',{'list':list})

@login_teacher_required(login_url="/teacherPlan/login")
def makePDF(request,id=1):
    response = HttpResponse(content_type='application/pdf')
    try:
        tp = TeacherPlan.objects.get(id=id)
    except:
        raise Http404
    somefilename = "teacher plan " + tp.id
    print somefilename
    response['Content-Disposition'] = 'attachment; filename="' + somefilename + '.pdf"'

    return conclusion_to_pdf(response,id)

##SECTION TP forms
@login_teacher_required(login_url="/teacherPlan/login")
def studybookList(request, id=1):
    #todo исправить проблемы в модели
    try:
        plan = TeacherPlan.objects.get(id=id)[0]
    except:
        raise Http404
    if request.method == 'POST':
        return HttpResponseRedirect("")
    else:

        books = plan.study_books
        return render(request, 'teacherPlan/forms/1_studybook_list.html', {'form': StudyBookForm,'books':books})

@login_teacher_required(login_url="/teacherPlan/login")
def disciplineList(request, id=1):
    try:
        tp = TeacherPlan.objects.get(id=id)
    except:
         raise Http404
    if request.method == 'POST':
        form = AcademicDisciplineForm(request.POST)
        if form.is_valid():
            newdisc = AcademicDiscipline.objects.create(
                name=request.POST['name'],
                type=request.POST['type'],
                characterUpdate=request.POST['characterUpdate'])

            tp.disciplines =  tp.disciplines + [newdisc]
            tp.save()

        return HttpResponseRedirect('/teacherPlan/disciplineList/' + tp.id)
    else:
        disciplines = tp.disciplines
    return render(request,
                  'teacherPlan/forms/2_discipline_list.html',
                  {'form':AcademicDisciplineForm,
                   'disciplines':disciplines})


@login_teacher_required(login_url="/teacherPlan/login")
def scWorkList(request, id=1):
    try:
        tp = TeacherPlan.objects.get(id=id)
    except:
         raise Http404
    if request.method == 'POST':
        form = ScientificWorkForm(request.POST)
        if form.is_valid():
            newNIR = NIR.objects.create(
                name=request.POST['name'],
                period=request.POST['period'],
                role=request.POST['role'],
                organisation=request.POST['organisation'],
            )
            tp.NIRS =  tp.NIRS + [newNIR]
            tp.save()

        return HttpResponseRedirect('/teacherPlan/scWorkList/' + tp.id)
    else:
        nirs = tp.NIRS
    return render(request, 'teacherPlan/forms/3_sc_work_list.html',
                  {'form':ScientificWorkForm,'nirs':nirs})

@login_teacher_required(login_url="/teacherPlan/login")
def participationList(request, id=1):
    try:
        tp = TeacherPlan.objects.get(id=id)
    except:
         raise Http404
    if request.method == 'POST':
        form = ParticipationForm(request.POST)
        if form.is_valid():
            newParticipation = Participation.objects.create(
                name=request.POST['name'],
                date=request.POST['date'],
                level=request.POST['level'],
                report=request.POST['report'],
            )
            tp.participations =  tp.participations + [newParticipation]
            tp.save()

        return HttpResponseRedirect('/teacherPlan/participationList/' + tp.id)
    else:
        participations = tp.participations
    return render(request, 'teacherPlan/forms/4_participation_list.html',
                  {'form':ParticipationForm,'participations':participations})

@login_teacher_required(login_url="/teacherPlan/login")
def publicationList(request, id=1):
    try:
        tp = TeacherPlan.objects.get(id=id)
    except:
         raise Http404
    if request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():
            newTeacherPublication = TeacherPublication.objects.create(
                name_work=request.POST['name_work'],
                type=request.POST['type'],
                volume=request.POST['volume'],
                name_publisher=request.POST['name_publisher'],
            )
            tp.publications =  tp.publications + [newTeacherPublication]
            tp.save()

        return HttpResponseRedirect('/teacherPlan/publicationList/' + tp.id)
    else:
        publications = tp.publications
    return render(request, 'teacherPlan/forms/5_publication_list.html',
                  {'form':PublicationForm,'publications':publications})
@login_teacher_required(login_url="/teacherPlan/login")
def qualificationList(request, id=1):
    try:
        tp = TeacherPlan.objects.get(id=id)
    except:
         raise Http404
    if request.method == 'POST':
        form = QualificationForm(request.POST)
        if form.is_valid():
            newdisc = Qualification.objects.create(
                ql_date=request.POST['ql_date'],
                for_ql=request.POST['for_ql'],
                doc=request.POST['doc'],
            )
            tp.qualifications =  tp.qualifications + [newdisc]
            tp.save()

        return HttpResponseRedirect('/teacherPlan/qualificationList/' + tp.id)
    else:
        qualifications = tp.qualifications
    return render(request, 'teacherPlan/forms/6_qualification_list.html',
                  {'form':QualificationForm,'qualifications':qualifications})

@login_teacher_required(login_url="/teacherPlan/login")
def difWorkList(request, id=1):
    try:
        tp = TeacherPlan.objects.get(id=id)
    except:
         raise Http404
    if request.method == 'POST':
        form = AnotherWorkForm(request.POST)
        if form.is_valid():
            newdisc = AnotherWork.objects.create(
                work_date=request.POST['work_date'],
                v_work=request.POST['v_work'])

            tp.anotherworks =  tp.anotherworks + [newdisc]
            tp.save()

        return HttpResponseRedirect('/teacherPlan/difWorkList/' + tp.id)
    else:
        anotherworks = tp.anotherworks
    return render(request, 'teacherPlan/forms/7_dif_work_list.html',
                  {'form':AnotherWorkForm,
                  'anotherworks':anotherworks})

## END SECTION TP forms

