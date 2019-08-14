# coding:utf-8

from django import forms
from cronjob.model import CronjobStateModel, format_html
from django.utils.translation import ugettext as _

class CronjobStateForm(forms.ModelForm):

    class Meta:
        model = CronjobStateModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CronjobStateForm, self).__init__(*args, **kwargs)

