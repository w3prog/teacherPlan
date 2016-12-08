#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import admin
from moevmCommon.models.userProfile import UserProfile
from moevmCommon.models.academicDiscipline import AcademicDiscipline,AcademicDisciplineOfTeacher
from moevmCommon.models.nir import NIR
from moevmCommon.models.publication import Publication
from moevmCommon.models.scientificEvent import ScientificEvent,Participation


admin.site.register(UserProfile)
admin.site.register(AcademicDiscipline)
admin.site.register(AcademicDisciplineOfTeacher)
admin.site.register(NIR)
admin.site.register(ScientificEvent)
admin.site.register(Participation)
admin.site.register(Publication)