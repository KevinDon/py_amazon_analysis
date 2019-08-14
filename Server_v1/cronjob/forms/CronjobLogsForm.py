# coding:utf-8

from django import forms
from cronjob.model import CronjobLogsModel
from django.utils.translation import ugettext as _

class CronjobLogsForm(forms.ModelForm):

    class Meta:
        model = CronjobLogsModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CronjobLogsForm, self).__init__(*args, **kwargs)


