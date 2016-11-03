from django.conf.urls import patterns, url
from django.conf.urls import url, include
from django.contrib.contenttypes import views as contenttype_views
from views import *
urlpatterns = patterns('',
   url(r'^$', index, name='tpindex'),
   url(r'^registration$', reqistration, name='tpregistration', ),
   url(r'^listOfPlans$', listOfPlans, name='tpplanlist', ),
   url(r'^makeNewPlan$', makeNewPlan, name='tpnewPlan', ),
   url(r'^plan$', plan, name='tpplan', ),
   url(r'^managerReport$', managerReport, name='tpsimpleReport')
                       )