# coding:utf-8

from django import forms
from django.utils.translation import ugettext as _
from django.core.handlers.base import logger

from system.model import ServerConfigModel
from dictionary.model import *
from django.forms import fields, widgets


class ServerConfigForm(forms.ModelForm):

    class Meta:
        model = ServerConfigModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ServerConfigForm, self).__init__(*args, **kwargs)
        self.fields['timezone'].required = False
        self.fields['api_account'].required = False
        self.fields['api_password'].required = False
        self.fields['max_process'].required = False
        self.fields['process'].required = False
        self.fields['remark'].required = False

