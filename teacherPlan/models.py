#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from djangotoolbox.fields import EmbeddedModelField, ListField

#from moevmCommon.models.userProfile import UserProfile

class TeacherPlan(models.Model):
#  teacher = models.OneToOneField(UserProfile)
  date = models.DateField(null=True)

  research = ListField(EmbeddedModelField('Publication'))
  disciplines = ListField(EmbeddedModelField('Comment'))
  Participations = ListField(EmbeddedModelField('Comment'))
  nirs = ListField(EmbeddedModelField('Comment'))

  @property
  def teacher_name(self):
    return self.teacher.first_name + " " + self.teacher.last_name

  def __str__(self):
    return "Учебный план на " + self.date + " " + self.teacher_name

class Qualification(models.Model):
  ql_date = models.DateTimeField(verbose_name="Период")
  for_ql = models.CharField(max_length=200, verbose_name="Форма повышения квалификации")
  doc = models.CharField(max_length=200, verbose_name="Документ")

class AnotherWork(models.Model):
  work_date = models.DateTimeField(verbose_name="Период")
  v_work = models.CharField(max_length=200, verbose_name="Вид работы")

class Remark(models.Model):
  rem_date = models.DateTimeField(verbose_name="Дата")
  rem = models.CharField(max_length=200, verbose_name="Характер замечания")
  position = models.CharField(max_length=200, verbose_name="Должность лица, вносящего замечание")
  # sign = models.CharField(max_length=200, verbose_name="Подпись лица, вносящего замечание")
  # sign_t = models.CharField(max_length=200, verbose_name="Подпись преподавателя")