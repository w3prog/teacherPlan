#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import admin

from teacherPlan.models import Settings

admin.AdminSite.register(Settings)