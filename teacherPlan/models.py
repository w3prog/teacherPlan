#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from djangotoolbox.fields import EmbeddedModelField, ListField

@python_2_unicode_compatible
class TeacherSettings(models.Model):
    department_name = models.CharField(
        verbose_name="Название кафедры",
        max_length=10,
        null=True,
        blank=True,
    )
    organisation_name = models.CharField(
        verbose_name="Название факультета",
        max_length=10,
        null=True,
        blank=True,
    )
    department_head = models.CharField(
        verbose_name="Заведующий кафедры",
        max_length=100,
        null=True,
        blank=True,
    )
    organisation_head = models.CharField(
        verbose_name="Декан",
        max_length=100,
        null=True,
        blank=True,
    )
    @staticmethod
    def get():
        try:
            return TeacherSettings.objects.first()
        except:
            return TeacherSettings.objects.create(
                department_name=u"Кафедра",
                organisation_name=u"Факультет",
                department_head=u"Зав. Кафедры",
                organisation_head=u"Декан",
            )

    def __str__(self):
        return u"Основные настройки"