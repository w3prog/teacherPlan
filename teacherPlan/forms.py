#!/usr/bin/python
# -*- coding: utf-8 -*-
from django import forms
from moevmCommon.models import *
from moevmCommon.models import nir
from moevmCommon.models import publication
from moevmCommon.models import publication
from moevmCommon.models.academicDiscipline import AcademicDiscipline, AcademicDisciplineOfTeacher
from moevmCommon.models.scientificEvent import ScientificEvent
from teacherPlan.models import AnotherWork, Remark, Qualification, Conf


class NirForm(forms.ModelForm):
    class Meta:
        model=nir
        fields=('workName','startDate','finishDate','role','organisation')

# class PublicationForm(forms.ModelForm):
#    class Meta:
#        model=publication
#        #fields=('name_mw', 'edition', 'volume', 'requisite', 'mw_date', 'realization')

class AcademicDisciplineForm(forms.ModelForm):
    class Meta:
        model=AcademicDisciplineOfTeacher
        fields=('name','period','partaker','organization')

class ScientificEventForm(forms.ModelForm):
     class Meta:
        model = ScientificEvent
        #fields = ('name_disc', 'occ', 'change', 'realization')

# class PublicationForm(forms.ModelForm):
#      class Meta:
#         model = publication
#         #fields = ('name_work', 'publications', 'volume', 'name_publisher')

class AnotherWorkForm(forms.ModelForm):
     class Meta:
        model = AnotherWork
        fields = ('work_date', 'v_work')

class RemarkForm(forms.ModelForm):
     class Meta:
        model = Remark
        fields = ('rem_date', 'rem', 'position', 'sign', 'sign_t')

class QualificationForm(forms.ModelForm):
     class Meta:
        model = Qualification
        fields = ('ql_date', 'for_ql', 'doc')

class ConfForm(forms.ModelForm):
    class Meta:
        model=Conf
        #fields=('conf_date','name_conf','level_conf','name_rep')