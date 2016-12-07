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


class MethodicalWork(models.Model):
  name_mw = models.CharField(max_length=200, verbose_name="Наименование")
  edition = models.CharField(max_length=200, verbose_name="Вид издания")
  volume = models.CharField(max_length=200, verbose_name="Объем")
  requisite = models.CharField(max_length=200, verbose_name="Вид грифа")
  mw_date = models.DateTimeField(verbose_name="Срок сдачи рукописи")
  realization = models.BooleanField(verbose_name="Отметка о выполнении")


class StConf(models.Model):
  name_work = models.CharField(max_length=200, verbose_name="Наименование конференции")
  period = models.DateTimeField(verbose_name="Дата")
  partaker = models.CharField(max_length=200, verbose_name="Уровень конференции")
  organization = models.CharField(max_length=200, verbose_name="В качестве кого участвовал")


class Modern(models.Model):
  name_disc = models.CharField(max_length=200, verbose_name="Наименование дисциплины")
  occ = models.CharField(max_length=200, verbose_name="Вид занятия")
  change = models.CharField(max_length=200, verbose_name="Характер изменения")
  realization = models.BooleanField(verbose_name="Отметка о выполнении")


class Publication(models.Model):
  name_work = models.CharField(max_length=200, verbose_name="Наименование работ")
  publications = models.CharField(max_length=200, verbose_name="Список публикаций")
  volume = models.CharField(max_length=200, verbose_name="Объем")
  name_publisher = models.CharField(max_length=200, verbose_name="Наименование издательства")


class AnotherWork(models.Model):
  work_date = models.DateTimeField(verbose_name="Период")
  v_work = models.CharField(max_length=200, verbose_name="Вид работы")


class Qualification(models.Model):
  ql_date = models.DateTimeField(verbose_name="Период")
  for_ql = models.CharField(max_length=200, verbose_name="Форма повышения квалификации")
  doc = models.CharField(max_length=200, verbose_name="Документ")


class Remark(models.Model):
  rem_date = models.DateTimeField(verbose_name="Дата")
  rem = models.CharField(max_length=200, verbose_name="Характер замечания")
  position = models.CharField(max_length=200, verbose_name="Должность лица, вносящего замечание")
  sign = models.CharField(max_length=200, verbose_name="Подпись лица, вносящего замечание")
  sign_t = models.CharField(max_length=200, verbose_name="Подпись преподавателя")


class Study(models.Model):
  name_work = models.CharField(max_length=200, verbose_name="Наименование работы")
  period = models.CharField(max_length=200, verbose_name="Период")
  partaker = models.CharField(max_length=200, verbose_name="В качестве кого участвовал")
  organization = models.CharField(max_length=200, verbose_name="Организация или предприятие")



class Conf(models.Model):
    conf_date = models.DateTimeField(verbose_name="Дата")
    name_conf = models.CharField(max_length=200, verbose_name="Наименование конференции")
    level_conf=models.CharField(max_length=200, verbose_name="Уровень конференции")
    name_rep = models.CharField(max_length=200, verbose_name="Наименование доклада")