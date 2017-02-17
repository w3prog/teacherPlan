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
   url(r'^plan/(?P<id>[0-9a-z]+)$', plan, name='tpplan', ),
   url(r'^currentPlan/', currentPlan, name='currentPlan', ),
   url(r'^plan/add/',makeNewPlan , name='addPlan'),
   url(r'^allplans/',show_all_plan,name='showAllPlans'),

   url(r'^registerTeacher/', registerTeacher, name='registerTeacher' ),


   #forms_edit
   url(r'^studybookList/(?P<id>[0-9a-z]+)/edit', studybook_list_edit, name='studybookListEdit'),
   url(r'^disciplineList/(?P<id>[0-9a-z]+)/edit', discipline_list_edit, name='disciplineListEdit'),
   url(r'^scWorkList/(?P<id>[0-9a-z]+)/edit', scWorkList_edit, name='scWorkListEdit'),
   url(r'^participationList/(?P<id>[0-9a-z]+)/edit', participation_list_edit, name='participationListEdit'),
   url(r'^publicationList/(?P<id>[0-9a-z]+)/edit', publication_list_edit, name='publicationListEdit'),
   url(r'^qualificationList/(?P<id>[0-9a-z]+)/edit', qualification_list_edit, name='qualificationListEdit'),
   url(r'^difWorkList/(?P<id>[0-9a-z]+)/edit', dif_work_list_edit, name='difWorkListEdit'),

   #forms
   url(r'^studybookList/(?P<id>[0-9a-z]+)', studybook_list, name='studybookList'),
   url(r'^disciplineList/(?P<id>[0-9a-z]+)', discipline_list, name='disciplineList'),
   url(r'^scWorkList/(?P<id>[0-9a-z]+)', scWorkList, name='scWorkList'),
   url(r'^participationList/(?P<id>[0-9a-z]+)', participation_list, name='participationList'),
   url(r'^publicationList/(?P<id>[0-9a-z]+)', publication_list, name='publicationList'),
   url(r'^qualificationList/(?P<id>[0-9a-z]+)', qualification_list, name='qualificationList'),
   url(r'^difWorkList/(?P<id>[0-9a-z]+)', dif_work_list, name='difWorkList'),



   url(r'^pdf/(?P<id>[0-9a-z]+)', makePDF, name='pdf'),
)