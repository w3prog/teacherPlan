#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.conf.urls import url, include
from django.contrib.contenttypes import views as contenttype_views
from views import *





urlpatterns = patterns(
   '',
   url(r'^$', index, name='tpindex'),

   #auth
   url(r'^login$', loginTeacher, name='tplogin', ),
   url(r'^loginwitherror$', errorLoginTeacher, name='tploginwitherror', ),
   url(r'^logout$', logoutTeacher, name='tplogout', ),

   #plans
   url(r'^listOfPlans$', listOfPlans, name='tpplanlist', ),
   url(r'^makeNewPlan$', makeNewPlan, name='tpnewPlan', ),
   url(r'^plan/(?P<id>[0-9]+)$', plan, name='tpplan', ),
   url(r'^currentPlan/', currentPlan, name='currentPlan', ),

   #forms
   url(r'^pdf/(?P<id>[0-9]+)', makePDF, name='pdf'),
   url(r'^difWorkList/(?P<id>[0-9]+)', difWorkList, name='difWorkList'),
   url(r'^disciplineList/(?P<id>[0-9]+)', disciplineList, name='disciplineList'),
   url(r'^participationList/(?P<id>[0-9]+)', participationList, name='participationList'),
   url(r'^publicationList/(?P<id>[0-9]+)', publicationList, name='publicationList'),
   url(r'^qualificationList/(?P<id>[0-9]+)', qualificationList, name='qualificationList'),
   url(r'^remarkList/(?P<id>[0-9]+)', remarkList, name='remarkList'),
   url(r'^scWorkList/(?P<id>[0-9]+)', scWorkList, name='scWorkList'),
   url(r'^studybookList/(?P<id>[0-9]+)', studybookList, name='studybookList'),

   #for managers
   url(r'^managerReport$', managerReport, name='tpsimpleReport'),
)