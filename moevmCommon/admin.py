#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import admin
from moevmCommon.models import *
admin.site.register(StudyBook)
admin.site.register(AcademicDiscipline)
admin.site.register(NIR)
admin.site.register(Participation)
admin.site.register(TeacherPublication)
admin.site.register(Qualification)
admin.site.register(AnotherWork)




admin.site.register(UserProfile)
# В данный момент не готово
#admin.site.register(TeacherPlan)