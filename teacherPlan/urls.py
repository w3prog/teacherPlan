from django.conf.urls import patterns, url
from django.conf.urls import url, include
from django.contrib.contenttypes import views as contenttype_views
from views import *





urlpatterns = patterns(
   '',
   url(r'^$', index, name='tpindex'),
   url(r'^login$', loginTeacher, name='tplogin', ),
   url(r'^loginwitherror$', errorLoginTeacher, name='tploginwitherror', ),
   url(r'^logout$', logoutTeacher, name='tplogout', ),
   url(r'^listOfPlans$', listOfPlans, name='tpplanlist', ),
   url(r'^makeNewPlan$', makeNewPlan, name='tpnewPlan', ),
   url(r'^plan$', plan, name='tpplan', ),

   url(r'^pdf/(?P<id>[0-9]{4})', makePDF, name='pdf'),
   #for managers
   url(r'^managerReport$', managerReport, name='tpsimpleReport'),
)