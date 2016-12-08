#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from moevmCommon.models.userProfile import UserProfile

class AcademicDiscipline(models.Model):
  name = models.CharField(
    max_length=150,
    verbose_name="Наименование дисциплины",
  )

  @staticmethod
  def create(**params):
    academicDiscipline = AcademicDiscipline.objects.create(
      name=params.get('name'),

    )
    academicDiscipline.save()

    return academicDiscipline

  def __str__(self):
    return self.name


class AcademicDisciplineOfTeacher(models.Model):
  teacher = models.ForeignKey(
    UserProfile,
    verbose_name="Преподаватель",
  )
  disc = models.ForeignKey(
    AcademicDiscipline,
    verbose_name="Дисциплины",
  )
  type = models.CharField(
    max_length=40,
    null=True,
    verbose_name="Вид занятия",
  )
  characterUpdate = models.CharField(
    max_length=250,
    null=True,
    verbose_name="Характер обновления",
  )
  completeMark = models.BooleanField(
    default=False,
    null=True,
    verbose_name="Отметка о завершении",
  )

  @staticmethod
  def create(**params):
    academicDisciplineOfTeacher = AcademicDisciplineOfTeacher.objects.create(
      teacher=params.get('teacher'),
      disc=params.get('disc'),
      type=params.get('type'),
      characterUpdate=params.get('characterUpdate'),
      completeMark=params.get('completeMark'),
    )
    academicDisciplineOfTeacher.save()

    return academicDisciplineOfTeacher

  def __str__(self):
    return self.teacher + " " + self.disc