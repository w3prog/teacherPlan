#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from moevmCommon.models.userProfile import UserProfile

class NIR(models.Model):
  user = models.ForeignKey(
    UserProfile,
    verbose_name="Сотрудник",
  )
  workName = models.CharField(
    max_length=250,
    verbose_name="Название работ",
  )
  startDate = models.DateField(
    null=True,
    verbose_name="Дата начала работ",
  )
  finishDate = models.DateField(
    null=True,
    verbose_name="Дата конца работ",
  )
  role = models.CharField(
    max_length=100,
    null=True,
    verbose_name="Должность",
  )
  organisation = models.CharField(
    max_length=250,
    null=True,
    verbose_name="Организация",
  )
  cipher = models.CharField(
    max_length="100",
    null=True,
    verbose_name = "Шифр",
  )

  @staticmethod
  def create(**params):
    nir = NIR.objects.create(
      user=params.get('user'),
      startDate=params.get('startDate'),
      finishDate = params.get('finishDate'),
      role = params.get('role'),
      organisation = params.get('organisation'),
      cipher = params.get('cipher'),
    )

    nir.save()

    return nir

  def __str__(self):
    return self.workName + " " + self.organisation + " " + self.cipher