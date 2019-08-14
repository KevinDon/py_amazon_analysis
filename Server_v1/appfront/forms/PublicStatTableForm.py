# coding:utf-8

from django import forms
from django.utils.translation import ugettext as _
from appfront.model.PublicStatModel import *

class PubStatDaysForm(forms.ModelForm):
    class Meta:
        model = PubStatDaysModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PubStatDaysForm, self).__init__(*args, **kwargs)

    def has_change_permission(self, request):
        """ 取消后台编辑附件功能 """
        return False


class PubStatMonthForm(forms.ModelForm):
    class Meta:
        model = PubStatMonthModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PubStatMonthForm, self).__init__(*args, **kwargs)

    def has_change_permission(self, request):
        """ 取消后台编辑附件功能 """
        return False


class PubStatWeeksForm(forms.ModelForm):
    class Meta:
        model = PubStatWeeksModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PubStatWeeksForm, self).__init__(*args, **kwargs)

    def has_change_permission(self, request):
        """ 取消后台编辑附件功能 """
        return False


