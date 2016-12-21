#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import admin
from moevmCommon.models import *


admin.site.register(UserProfile)
admin.site.register(AcademicDiscipline)
admin.site.register(NIR)
admin.site.register(ScientificEvent)
admin.site.register(Participation)
admin.site.register(Publication)
admin.site.register(TeacherPlan)