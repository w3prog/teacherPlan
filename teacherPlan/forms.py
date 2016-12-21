#!/usr/bin/python
# -*- coding: utf-8 -*-
from django import forms
from django.forms import CharField,\
  DateField,\
  IntegerField,\
  ModelForm, ChoiceField, EmailField
from moevmCommon.models import *
from moevmCommon.models import ACADEMIC_DEGREE_CHOICES,\
  ACADEMIC_STATE_CHOICES,ACADEMIC_STATUS_CHOICES
from moevmCommon.models import AnotherWork, Qualification

#SECTION form for teacherPlan
class StudyBookForm(forms.Form):
  name = CharField(max_length=200, label="Наименование")
  type = CharField(max_length=200, label="Вид издания")
  volume = CharField(max_length=200, label="Объем")
  vulture = CharField(max_length=200, label="Вид грифа")
  finishDate = CharField(label="Срок сдачи рукописи")

class AcademicDisciplineForm(forms.Form):
  name = CharField(max_length=200, label="Наименование дисциплины")
  type = CharField(max_length=200, label="Вид занятия")
  characterUpdate = CharField(max_length=200, label="Характер изменения")

class ScientificWorkForm(forms.Form):
  name = CharField(max_length=200, label="Наименование работы")
  period = CharField(max_length=200, label="Период")
  role = CharField(max_length=200, label="В качестве кого участвовал")
  organisation = CharField(max_length=200, label="Организация или предприятие")

class ParticipationForm(forms.Form):
  name = CharField(max_length=200, label="Наименование конференции")
  level = CharField(max_length=200, label="Уровень конференции")
  report = CharField(max_length=200, label="Наименование доклада")
  date = CharField(max_length=30,label="Дата")

class PublicationForm(forms.Form):
  name_work = CharField(max_length=200, label="Наименование работ")
  type = CharField(max_length=200, label="Вид публикации")
  volume = IntegerField(label="Объем в п.л.")
  name_publisher = CharField(max_length=200, label="Наименование издательства")

class QualificationForm(ModelForm):
  class Meta:
    model = Qualification
    fields = ('ql_date', 'for_ql', 'doc')

class AnotherWorkForm(ModelForm):
  class Meta:
    model = AnotherWork
    fields = ('work_date', 'v_work')

# END SECTION
class RegisterTeacherForm(forms.Form):
  username = CharField(
    label='Логин',
    max_length=100,
    required=True,
  )
  email = EmailField(
    label="Email",
    max_length=100,
    required = True,
  )
  password = CharField(
    label="Пароль",
    max_length=100,
    required=True,
  )
  first_name = CharField(
    label="Имя",
    max_length=100,
    required=True,
  )
  last_name = CharField(
    label="Фамилия",
    max_length=100,
    required=True,
  )
  patronymic = CharField(
    label="Отчество",
    max_length=30,
  )
  birth_date = DateField(
    label="Дата рождения",
    required=True,
  )
  election_date = DateField(
    label="Дата текущего избрания или зачисления на преподавательскую должность",
  )
  position = CharField(
    label="Должность",
    max_length=40,
    required=True,
  )
  contract_date = DateField(
    label="Срок окончания трудового договора"
  )
  academic_degree = ChoiceField(
    label="Учебная степень",
    choices=ACADEMIC_DEGREE_CHOICES,
    required=True,
  )
  year_of_academic_degree = CharField(
    label="Год присвоения ученой степени"
  )
  academic_status = ChoiceField(
    label="Учебное звание",
    choices=ACADEMIC_STATUS_CHOICES,
    required=True,
  )
  year_of_academic_status = DateField(
    label="Год получения учебного звания"
  )
  academic_state = ChoiceField(
    label="Академическое положение",
    choices=ACADEMIC_STATE_CHOICES
  )
  github_id = CharField(
    label="Профиль github",
    max_length=100,
  )
  stepic_id = CharField(
    label="Профиль stepic",
    max_length=100,
  )