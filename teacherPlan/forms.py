#!/usr/bin/python
# -*- coding: utf-8 -*-
from django import forms
from moevmCommon.models import *
from moevmCommon.models import nir
from moevmCommon.models import publication
from moevmCommon.models.academicDiscipline import AcademicDiscipline, AcademicDisciplineOfTeacher
from moevmCommon.models.scientificEvent import ScientificEvent
from moevmCommon.models.userProfile import UserProfile,ACADEMIC_DEGREE_CHOICES,\
  ACADEMIC_STATE_CHOICES,ACADEMIC_STATUS_CHOICES
from teacherPlan.models import AnotherWork, Remark, Qualification

#SECTION form for teacherPlan
class StudyBookForm(forms.Form):
  #todo проверить совпадение размерностей
  name_mw = forms.CharField(max_length=200, label="Наименование")
  edition = forms.CharField(max_length=200, label="Вид издания")
  volume = forms.CharField(max_length=200, label="Объем")
  requisite = forms.CharField(max_length=200, label="Вид грифа")
  mw_date = forms.DateField(label="Срок сдачи рукописи")

class AcademicDisciplineForm(forms.Form):
  name_disc = forms.CharField(max_length=200, label="Наименование дисциплины")
  occ = forms.CharField(max_length=200, label="Вид занятия")
  change = forms.CharField(max_length=200, label="Характер изменения")

class ScWorkForm(forms.Form):
  name_work = forms.CharField(max_length=200, label="Наименование работы")
  period = forms.CharField(max_length=200, label="Период")
  partaker = forms.CharField(max_length=200, label="В качестве кого участвовал")
  organization = forms.CharField(max_length=200, label="Организация или предприятие")

class ParticipationForm(forms.Form):
  conf_date = forms.DateField(label="Дата")
  name_conf = forms.CharField(max_length=200, label="Наименование конференции")
  level_conf = forms.CharField(max_length=200, label="Уровень конференции")
  name_rep = forms.CharField(max_length=200, label="Наименование доклада")

class PublicationForm(forms.Form):
  name_work = forms.CharField(max_length=200, label="Наименование работ")
  publications = forms.CharField(max_length=200, label="Список публикаций")
  volume = forms.IntegerField(label="Объем")
  name_publisher = forms.CharField(max_length=200, label="Наименование издательства")

class QualificationForm(forms.ModelForm):
  class Meta:
    model = Qualification
    fields = ('ql_date', 'for_ql', 'doc')

class AnotherWorkForm(forms.ModelForm):
  class Meta:
    model = AnotherWork
    fields = ('work_date', 'v_work')

class RemarkForm(forms.ModelForm):
  class Meta:
    model = Remark
    fields = ('rem_date', 'rem', 'position')

# END SECTION
class RegisterTeacherForm(forms.Form):
  username = forms.CharField(
    label='Логин',
    max_length=100,
    required=True,
  )
  email = forms.EmailField(
    label="Email",
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
    label="Должность",
    max_length=40,
    required=True,
  )
  contract_date = forms.DateField(
    label="Срок окончания трудового договора"
  )
  academic_degree = forms.ChoiceField(
    label="Учебная степень",
    choices=ACADEMIC_DEGREE_CHOICES,
    required=True,
  )
  year_of_academic_degree = forms.CharField(
    label="Год присвоения ученой степени"
  )
  academic_status = forms.ChoiceField(
    label="Учебное звание",
    choices=ACADEMIC_STATUS_CHOICES,
    required=True,
  )
  year_of_academic_status = forms.DateField(
    label="Год получения учебного звания"
  )
  academic_state = forms.ChoiceField(
    label="Академическое положение",
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