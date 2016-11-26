# -*- coding: utf-8 -*-
from django import forms

from moevmCommon.models import *
from moevmCommon.models import nir
from moevmCommon.models import publication
from moevmCommon.models import publication
from moevmCommon.models.academicDiscipline import AcademicDiscipline
from moevmCommon.models.scientificEvent import ScientificEvent


class StConfForm(forms.ModelForm):
    class Meta:
        model=nir
        fields=('name_work','period','partaker','organization')



class MWForm(forms.ModelForm):
   class Meta:
       model=publication
       fields=('name_mw', 'edition', 'volume', 'requisite', 'mw_date', 'realization')




class StForm(forms.ModelForm):
    class Meta:
        model=AcademicDiscipline
        fields=('name_work','period','partaker','organization')




class ModernForm(forms.ModelForm):
     class Meta:
        model = ScientificEvent
        fields = ('name_disc', 'occ', 'change', 'realization')



class PublicationForm(forms.ModelForm):
     class Meta:
        model = publication
        fields = ('name_work', 'publications', 'volume', 'name_publisher')



# class AnotherWForm(forms.ModelForm):
#      class Meta:
#         model = AnotherW
#         fields = ('work_date', 'v_work')
#
#
#
# class RemarkForm(forms.ModelForm):
#      class Meta:
#         model = Remark
#         fields = ('rem_date', 'rem', 'position', 'sign', 'sign_t')
#
#
#
#
# class QualificationForm(forms.ModelForm):
#      class Meta:
#         model = Qualification
#         fields = ('ql_date', 'for_ql', 'doc')
# # class ConfForm(forms.ModelForm):
# #     class Meta:
# #         model=Conff
# #         fields=('conf_date','name_conf','level_conf','name_rep')