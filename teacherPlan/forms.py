#!/usr/bin/python
# -*- coding: utf-8 -*-
from django import forms
from moevmCommon.models import *
from moevmCommon.models import nir
from moevmCommon.models import publication
from moevmCommon.models import publication
from moevmCommon.models.academicDiscipline import AcademicDiscipline, AcademicDisciplineOfTeacher
from moevmCommon.models.scientificEvent import ScientificEvent
from moevmCommon.models.userProfile import UserProfile,ACADEMIC_DEGREE_CHOICES,\
  ACADEMIC_STATE_CHOICES,ACADEMIC_STATUS_CHOICES
from teacherPlan.models import AnotherWork, Remark, Qualification, Conf


class NirForm(forms.ModelForm):
    class Meta:
        model=nir
        fields=('workName','startDate','finishDate','role','organisation')

# class PublicationForm(forms.ModelForm):
#    class Meta:
#        model=publication
#        #fields=('name_mw', 'edition', 'volume', 'requisite', 'mw_date', 'realization')

class AcademicDisciplineForm(forms.ModelForm):
    class Meta:
        model=AcademicDisciplineOfTeacher
        fields=('name','period','partaker','organization')

class ScientificEventForm(forms.ModelForm):
     class Meta:
        model = ScientificEvent
        #fields = ('name_disc', 'occ', 'change', 'realization')

# class PublicationForm(forms.ModelForm):
#      class Meta:
#         model = publication
#         #fields = ('name_work', 'publications', 'volume', 'name_publisher')

class AnotherWorkForm(forms.ModelForm):
     class Meta:
        model = AnotherWork
        fields = ('work_date', 'v_work')

class RemarkForm(forms.ModelForm):
     class Meta:
        model = Remark
        fields = ('rem_date', 'rem', 'position', 'sign', 'sign_t')

class QualificationForm(forms.ModelForm):
     class Meta:
        model = Qualification
        fields = ('ql_date', 'for_ql', 'doc')

class ConfForm(forms.ModelForm):
    class Meta:
        model=Conf
        #fields=('conf_date','name_conf','level_conf','name_rep')

class RegisterTeacherForm(forms.Form):
  username = forms.CharField(
    label='login',
    max_length=100,
    required=True,
  )
  email = forms.CharField(
    label="email",
    max_length=100,
    required = True,
  )
  password = forms.CharField(
    label="Пароль",
    max_length=100,
    required=True,
  )
  first_name = forms.CharField(
    label="Имя",
    max_length=100,
    required=True,
  )
  last_name = forms.CharField(
    label="Фамилия",
    max_length=100,
    required=True,
  )
  patronymic = forms.CharField(
    label="Отчество",
    max_length=30,
  )
  birth_date = forms.DateField(
    label="Дата рождения",
    required=True,
  )
  election_date = forms.DateField(
    label="Дата текущего избрания или зачисления на преподавательскую должность",
  )
  position = forms.CharField(
    "Должность",
    max_length=40,
    required=True,
  )
  contract_date = forms.DateField(
    label="Срок окончания трудового договора"
  )
  academic_degree = forms.ChoiceField(
    max_length=2,
    choices=ACADEMIC_DEGREE_CHOICES,
    required=True,
  )
  year_of_academic_degree = forms.CharField(
    label="Год присвоения ученой степени"
  )
  academic_status = forms.ChoiceField(
    max_length=2,
    choices=ACADEMIC_STATUS_CHOICES,
    required=True,
  )
  year_of_academic_status = forms.DateField(
    label="Год получения учебного звания"
  )
  academic_state = forms.ChoiceField(
    max_length=2,
    choices=ACADEMIC_STATE_CHOICES
  )
  github_id = forms.CharField(
    label="Профиль github",
    max_length=100,
  )
  stepic_id = forms.CharField(
    label="Профиль stepic",
    max_length=100,
  )