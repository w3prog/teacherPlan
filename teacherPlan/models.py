#!/usr/bin/python
# -*- coding: utf-8 -*-
# Create your models here.
from django.db import models
from djangotoolbox.fields import EmbeddedModelField, ListField

from moevmCommon.models.userProfile import UserProfile

class teacherPlan(models.Model):
  teacher = models.OneToOneField(UserProfile)
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