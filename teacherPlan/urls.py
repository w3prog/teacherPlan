def get_urls():
    from django.conf.urls import url, include
    from django.contrib.contenttypes import views as contenttype_views
    from views import *
    urlpatterns = [
        url(r'^$', index, name='index'),
        url(r'^registration$', reqistration, name='registration', ),
        url(r'^listOfPlans$', listOfPlans, name='planlist', ),
        url(r'^makeNewPlan$', makeNewPlan, name='newPlan', ),
        url(r'^plan$', plan, name='plan', ),
        url(r'^managerReport$',managerReport,name='simpleReport')
    ]
    return urlpatterns

