# coding:utf-8

from django import forms
from cronjob.model import CronjobModel
from django.utils.translation import ugettext as _
from cronjob.widgets.CronjobWidget import *


class CronjobForm(forms.ModelForm):

    command_type = forms.IntegerField(widget=CronjobCommandTypeWidget(choices= tuple([('', _('Please choose ...'))] + list(CronjobModel.CHOICES_COMMANDTYPE)) ))

    class Meta:
        model = CronjobModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CronjobForm, self).__init__(*args, **kwargs)
        self.fields['timezone'].required = False
        self.fields['rule_id'].required = False

    def clean_code(self):
        code = self.cleaned_data.get('code')
        return code.upper()

