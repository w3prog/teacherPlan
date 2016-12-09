#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from djangotoolbox.fields import EmbeddedModelField, ListField


@python_2_unicode_compatible
class Qualification(models.Model):
  ql_date = models.DateTimeField(verbose_name="Период")
  for_ql = models.CharField(max_length=200, verbose_name="Форма повышения квалификации")
  doc = models.CharField(max_length=200, verbose_name="Документ")

@python_2_unicode_compatible
class AnotherWork(models.Model):
  work_date = models.DateTimeField(verbose_name="Период")
  v_work = models.CharField(max_length=200, verbose_name="Вид работы")

@python_2_unicode_compatible
class Remark(models.Model):
  rem_date = models.DateTimeField(verbose_name="Дата")
  rem = models.CharField(max_length=200, verbose_name="Характер замечания")
  position = models.CharField(max_length=200, verbose_name="Должность лица, вносящего замечание")