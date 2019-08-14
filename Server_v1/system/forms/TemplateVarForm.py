# coding:utf-8

from django import forms
from django.utils.translation import ugettext as _
from django.core.handlers.base import logger

from system.model import TemplateVarModel
from dictionary.model import *
from django.forms import fields, widgets


class TemplateVarForm(forms.ModelForm):
    message_type = fields.CharField(widget=widgets.SelectMultiple(choices=[]), required=False)

    class Meta:
        model = TemplateVarModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TemplateVarForm, self).__init__(*args, **kwargs)
        self.fields["message_type"].widget.choices = []
        try:
            dictionary = DataDictionaryModel.objects.get(code_main='message_type')
            self.fields["message_type"].widget.choices += DataDictionaryValueModel.objects.filter(dict_id=dictionary.id).values_list('value', 'title')
            if self.instance.message_type:
                self.initial["message_type"] = eval(self.instance.message_type)
        except Exception:
            pass
