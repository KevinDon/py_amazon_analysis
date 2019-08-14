# coding:utf-8

from django import forms
from cronjob.model import CronjobConfigModel, format_html
from django.utils.translation import ugettext as _

class CronjobConfigForm(forms.ModelForm):

    class Meta:
        model = CronjobConfigModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CronjobConfigForm, self).__init__(*args, **kwargs)

