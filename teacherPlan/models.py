#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from djangotoolbox.fields import EmbeddedModelField, ListField

@python_2_unicode_compatible
class Settings(models.Model):
    department_name = models.CharField(name="Название кафедры", max_length=10)
    organisation_name = models.CharField(name="Название факультета", max_length=10)
    department_head = models.CharField(name="Заведующий кафедры", max_length=100)
    organisation_head = models.CharField(name="Декан", max_length=100)
    @staticmethod
    def get():
        return Settings.objects.first()