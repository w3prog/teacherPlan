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
from bson.objectid import ObjectId
from django.db import connections



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
            return HttpResponseRedirect('/teacherPlan/loginwitherror')
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
    somefilename = "teacher_plan_" + tp.id
    response['Content-Disposition'] = 'attachment; filename="' + somefilename + '.pdf"'

    return conclusion_to_pdf(response,id)

##SECTION TP FROM
@login_teacher_required(login_url="/teacherPlan/login")
def studybook_list(request, id=1):
    try:
        tp = TeacherPlan.objects.get(id=id)
    except:
         raise Http404
    form = StudyBookForm
    if request.method == 'POST':
        if not 'delete' in request.POST:
            form = StudyBookForm(request.POST)
            if form.is_valid():
                newdisc = StudyBook.objects.create(
                    name=request.POST['name'],
                    type=request.POST['type'],
                    volume=request.POST['volume'],
                    vulture=request.POST['vulture'],
                    finishDate=request.POST['finishDate'],
                )
                tp.study_books = tp.study_books + [newdisc]
                tp.save()
                return HttpResponseRedirect('/teacherPlan/studybookList/' + tp.id)
        elif request.POST['delete'] == 'delete':
                array = []
                for i in tp.study_books:
                    if not i.id == request.POST['id']:
                        array.append(i)
                tp.study_books = array
                tp.save()
                return HttpResponseRedirect('/teacherPlan/studybookList/' + tp.id)
    books = tp.study_books
    return render(
            request,
            'teacherPlan/forms/1_studybook_list.html',
            {
                'form': form,
                'books':books,
                'planid':tp.id
            }
        )

@login_teacher_required(login_url="/teacherPlan/login")
def discipline_list(request, id=1):
    try:
        tp = TeacherPlan.objects.get(id=id)
    except:
         raise Http404
    form = AcademicDisciplineForm
    if request.method == 'POST':
        if not 'delete' in request.POST:
            form = AcademicDisciplineForm(request.POST)
            if form.is_valid():
                newdisc = AcademicDiscipline.objects.create(
                    name=request.POST['name'],
                    type=request.POST['type'],
                    characterUpdate=request.POST['characterUpdate']
                )
                tp.disciplines = tp.disciplines + [newdisc]
                tp.save()
                return HttpResponseRedirect('/teacherPlan/disciplineList/' + tp.id)
        elif request.POST['delete'] == 'delete':
                array = []
                for i in tp.disciplines:
                    if not i.id == request.POST['id']:
                        array.append(i)
                tp.disciplines = array
                tp.save()
                return HttpResponseRedirect('/teacherPlan/disciplineList/' + tp.id)
    disciplines = tp.disciplines
    return render(
        request,
        'teacherPlan/forms/2_discipline_list.html',
        {
            'form':form,
            'disciplines':disciplines,
            'planid': tp.id
        }
    )

@login_teacher_required(login_url="/teacherPlan/login")
def scWorkList(request, id=1):
    try:
        tp = TeacherPlan.objects.get(id=id)
    except:
         raise Http404
    form = ScientificWorkForm
    if request.method == 'POST':
        if not 'type' in request.POST:
            form = ScientificWorkForm(request.POST)
            if form.is_valid():
                newNIR = NIR.objects.create(
                    name=request.POST['name'],
                    period=request.POST['period'],
                    role=request.POST['role'],
                    organisation=request.POST['organisation'],
                )
                tp.NIRS = tp.NIRS + [newNIR]
                tp.save()
                return HttpResponseRedirect('/teacherPlan/scWorkList/' + tp.id)
        elif request.POST['type'] == 'delete':
            array = []
            for i in tp.NIRS:
                if not i.id == request.POST['id']:
                    array.append(i)
            tp.NIRS = array
            tp.save()
            return HttpResponseRedirect('/teacherPlan/scWorkList/' + tp.id)
    nirs = tp.NIRS
    return render(
        request,
        'teacherPlan/forms/3_sc_work_list.html',
        {
            'form':form,
            'nirs':nirs,
            'planid': tp.id
        }
    )

@login_teacher_required(login_url="/teacherPlan/login")
def participation_list(request, id=1):
    try:
        tp = TeacherPlan.objects.get(id=id)
    except:
         raise Http404
    form = ParticipationForm
    if request.method == 'POST':
        if not 'type' in request.POST:
            form = ParticipationForm(request.POST)
            if form.is_valid():
                newParticipation = Participation.objects.create(
                    name=request.POST['name'],
                    date=request.POST['date'],
                    level=request.POST['level'],
                    report=request.POST['report'],
                )
                tp.participations = tp.participations + [newParticipation]
                tp.save()
                return HttpResponseRedirect('/teacherPlan/participationList/' + tp.id)
        elif request.POST['type'] == 'delete':
            array = []
            for i in tp.participations:
                if not i.id == request.POST['id']:
                    array.append(i)
            tp.participations = array
            tp.save()
            return HttpResponseRedirect('/teacherPlan/participationList/' + tp.id)
    participations = tp.participations
    return render(
        request,
        'teacherPlan/forms/4_participation_list.html',
        {
            'form':form,
            'participations':participations,
            'planid': tp.id
        }
    )

@login_teacher_required(login_url="/teacherPlan/login")
def publication_list(request, id=1):
    try:
        tp = TeacherPlan.objects.get(id=id)
    except:
         raise Http404
    form = PublicationForm
    if request.method == 'POST':
        if not 'delete' in request.POST:
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
        elif request.POST['delete'] == 'delete':
            array = []
            for i in tp.publications:
                if not i.id == request.POST['id']:
                    array.append(i)
            tp.publications = array
            tp.save()
            return HttpResponseRedirect('/teacherPlan/publicationList/' + tp.id)
    publications = tp.publications
    return render(
        request,
        'teacherPlan/forms/5_publication_list.html',
        {
            'form':form,
            'publications':publications,
            'planid': tp.id
        }
    )

@login_teacher_required(login_url="/teacherPlan/login")
def qualification_list(request, id=1):
    try:
        tp = TeacherPlan.objects.get(id=id)
    except:
         raise Http404
    form = QualificationForm
    if request.method == 'POST' :
        if not 'type' in request.POST:
            form = QualificationForm(request.POST)
            if form.is_valid():
                newdisc = Qualification.objects.create(
                    period=request.POST['period'],
                    form_training=request.POST['form_training'],
                    document=request.POST['document'],
                )
                tp.qualifications =  tp.qualifications + [newdisc]
                tp.save()
                return HttpResponseRedirect('/teacherPlan/qualificationList/' + tp.id)
        elif request.POST['type'] == 'delete':
            form = QualificationDeleteForm(request.POST)
            if form.is_valid():
                array = []
                for i in tp.qualifications:
                    if not i.id ==request.POST['id']:
                        array.append(i)
                tp.qualifications = array
                tp.save()
                return HttpResponseRedirect('/teacherPlan/qualificationList/' + tp.id)
    qualifications = tp.qualifications
    return render(
        request,
        'teacherPlan/forms/6_qualification_list.html',
        {
            'form':form,
            'qualifications':qualifications,
            'planid': tp.id
        }
    )

@login_teacher_required(login_url="/teacherPlan/login")
def dif_work_list(request, id=1):
    try:
        tp = TeacherPlan.objects.get(id=id)
    except:
         raise Http404
    form = AnotherWorkForm
    if request.method == 'POST':
        if not 'type' in request.POST:
            form = AnotherWorkForm(request.POST)
            if form.is_valid():
                newdisc = AnotherWork.objects.create(
                    work_date=request.POST['work_date'],
                    type_work=request.POST['type_work'])
                tp.anotherworks =  tp.anotherworks + [newdisc]
                tp.save()
            return HttpResponseRedirect('/teacherPlan/difWorkList/' + tp.id)
        elif request.POST['type'] == 'delete':
            array = []
            for i in tp.anotherworks:
                if not i.id ==request.POST['id']:
                    array.append(i)
            tp.anotherworks = array
            tp.save()
            return HttpResponseRedirect('/teacherPlan/difWorkList/' + tp.id)
    anotherworks = tp.anotherworks
    return render(
        request,
        'teacherPlan/forms/7_dif_work_list.html',
        {
            'form':form,
            'anotherworks':anotherworks,
            'planid': tp.id
        }
    )

##END SECTION TP FORMS

##SECTION TP FORMS EDIT
@login_teacher_required(login_url="/teacherPlan/login")
def studybook_list_edit(request, id=1):
    try:
        tp = TeacherPlan.objects.get(id=id)
    except:
         raise Http404
    form = StudyBookForm
    if request.method == 'POST':
        form = StudyBookForm(request.POST)
        if form.is_valid():
            newdisc = StudyBook.objects.create(
                name=request.POST['name'],
                type=request.POST['type'],
                volume=request.POST['volume'],
                vulture=request.POST['vulture'],
                finishDate=request.POST['finishDate'],
            )
            array = []
            for i in tp.study_books:
                if not i.id == request.POST['idlink']:
                    array.append(i)
                else:
                    array.append(newdisc)
            tp.study_books = array
            tp.save()
            return HttpResponseRedirect('/teacherPlan/studybookList/' + tp.id)

    target = None
    idlink = request.GET['idlink']
    for i in tp.study_books:
        if i.id == idlink:
            target = i
            break
    if target == None:
        raise Http404
    return render(
        request,
        'teacherPlan/forms/update/1_studybook_list.html',
        {
            'idlink': idlink,
            'form':form,
            'target':target,
            'planid': tp.id
        }
    )

@login_teacher_required(login_url="/teacherPlan/login")
def discipline_list_edit(request, id=1):
    try:
        tp = TeacherPlan.objects.get(id=id)
    except:
         raise Http404
    form = AcademicDisciplineForm
    if request.method == 'POST':
        form = AcademicDisciplineForm(request.POST)
        if form.is_valid():
            newdisc = AcademicDiscipline.objects.create(
                name=request.POST['name'],
                type=request.POST['type'],
                characterUpdate=request.POST['characterUpdate']
            )
            array = []
            for i in tp.disciplines:
                if not i.id == request.POST['idlink']:
                    array.append(i)
                else:
                    array.append(newdisc)
            tp.disciplines = array
            tp.save()
            return HttpResponseRedirect('/teacherPlan/disciplineList/' + tp.id)

    target = None
    idlink = request.GET['idlink']
    for i in tp.disciplines:
        if i.id == idlink:
            target = i
            break
    if target == None:
        raise Http404
    return render(
        request,
        'teacherPlan/forms/update/2_discipline_list.html',
        {
            'idlink': idlink,
            'form':form,
            'target':target,
            'planid': tp.id
        }
    )

@login_teacher_required(login_url="/teacherPlan/login")
def scWorkList_edit(request, id=1):
    try:
        tp = TeacherPlan.objects.get(id=id)
    except:
         raise Http404
    form = ScientificWorkForm
    if request.method == 'POST':
        form = ScientificWorkForm(request.POST)
        if form.is_valid():
            newNIR = NIR.objects.create(
                name=request.POST['name'],
                period=request.POST['period'],
                role=request.POST['role'],
                organisation=request.POST['organisation'],
            )
            array = []
            for i in tp.NIRS:
                if not i.id == request.POST['idlink']:
                    array.append(i)
                else:
                    array.append(newNIR)
            tp.NIRS = array
            tp.save()
            return HttpResponseRedirect('/teacherPlan/scWorkList/' + tp.id)

    target = None
    idlink = request.GET['idlink']
    for i in tp.NIRS:
        if i.id == idlink:
            target = i
            break
    if target == None:
        raise Http404
    return render(
        request,
        'teacherPlan/forms/update/3_sc_work_list.html',
        {
            'idlink': idlink,
            'form':form,
            'target':target,
            'planid': tp.id
        }
    )

@login_teacher_required(login_url="/teacherPlan/login")
def participation_list_edit(request, id=1):
    try:
        tp = TeacherPlan.objects.get(id=id)
    except:
         raise Http404
    form = ParticipationForm
    if request.method == 'POST':
        form = ParticipationForm(request.POST)
        if form.is_valid():
            newParticipation = Participation.objects.create(
                name=request.POST['name'],
                date=request.POST['date'],
                level=request.POST['level'],
                report=request.POST['report'],
            )
            array = []
            for i in tp.participations:
                if not i.id == request.POST['idlink']:
                    array.append(i)
                else:
                    array.append(newParticipation)
            tp.participations = array
            tp.save()
            return HttpResponseRedirect('/teacherPlan/participationList/' + tp.id)

    target = None
    idlink = request.GET['idlink']
    for i in tp.participations:
        if i.id == idlink:
            target = i
            break
    if target == None:
        raise Http404
    return render(
        request,
        'teacherPlan/forms/update/4_participation_list.html',
        {
            'idlink': idlink,
            'form':form,
            'target':target,
            'planid': tp.id
        }
    )

@login_teacher_required(login_url="/teacherPlan/login")
def publication_list_edit(request, id=1):
    try:
        tp = TeacherPlan.objects.get(id=id)
    except:
         raise Http404
    form = PublicationForm
    if request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():
            newTeacherPublication = TeacherPublication.objects.create(
                name_work=request.POST['name_work'],
                type=request.POST['type'],
                volume=request.POST['volume'],
                name_publisher=request.POST['name_publisher'],
            )
            array = []
            for i in tp.publications:
                if not i.id == request.POST['idlink']:
                    array.append(i)
                else:
                    array.append(newTeacherPublication)
            tp.publications = array
            tp.save()
            return HttpResponseRedirect('/teacherPlan/publicationList/' + tp.id)

    publ = None
    idlink = request.GET['idlink']
    for i in tp.publications:
        if i.id == idlink:
            publ = i
            break
    if publ == None:
        raise Http404
    return render(
        request,
        'teacherPlan/forms/update/5_publication_list.html',
        {
            'idlink': idlink,
            'form':form,
            'publ':publ,
            'planid': tp.id
        }
    )

@login_teacher_required(login_url="/teacherPlan/login")
def qualification_list_edit(request, id=1):
    try:
        tp = TeacherPlan.objects.get(id=id)
    except:
         raise Http404
    form = QualificationForm
    if request.method == 'POST':

        form = QualificationForm(request.POST)
        if form.is_valid():
            newdisc = Qualification.objects.create(
                period=request.POST['period'],
                form_training=request.POST['form_training'],
                document=request.POST['document'],
            )
            array = []
            for i in tp.qualifications:
                if not i.id == request.POST['idqual']:
                    array.append(i)
                else:
                    array.append(newdisc)
            tp.qualifications = array
            tp.save()
            return HttpResponseRedirect('/teacherPlan/qualificationList/' + tp.id)
    qualification=None
    idqual = request.GET['idqual']
    for i in tp.qualifications:
        if i.id == idqual:
            qualification = i
            break
    if qualification==None:
        raise Http404
    return render(
        request,
        'teacherPlan/forms/update/6_qualification_list.html',
        {
            'idqual':idqual,
            'form': form,
            'qualification': qualification,
            'planid': tp.id
        }
    )
@login_teacher_required(login_url="/teacherPlan/login")
def dif_work_list_edit(request, id=1):
    try:
        tp = TeacherPlan.objects.get(id=id)
    except:
         raise Http404
    form = AnotherWorkForm
    if request.method == 'POST':
        form = AnotherWorkForm(request.POST)
        if form.is_valid():
            newdisc = AnotherWork.objects.create(
                work_date=request.POST['work_date'],
                type_work=request.POST['type_work']
            )
            array = []
            for i in tp.anotherworks:
                if not i.id == request.POST['idaw']:
                    array.append(i)
                else:
                    array.append(newdisc)
            tp.anotherworks = array
            tp.save()
            return HttpResponseRedirect('/teacherPlan/difWorkList/' + tp.id)

    anotherwork=None
    idaw = request.GET['idaw']
    for i in tp.anotherworks:
        if i.id == idaw:
            anotherwork = i
            break
    if anotherwork==None:
        raise Http404
    return render(
        request,
        'teacherPlan/forms/update/7_dif_work_list.html',
        {
            'idaw':idaw,
            'form': form,
            'anotherwork': anotherwork,
            'planid': tp.id
        }
    )

##END SECTION TP FORMS EDIT

