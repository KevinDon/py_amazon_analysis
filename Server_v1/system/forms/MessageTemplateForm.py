# coding:utf-8

from django import forms
from django.utils.translation import ugettext as _
from django.core.handlers.base import logger

from system.model import MessageTemplateModel
from dictionary.model import *
from django.forms import fields, widgets


class MessageTemplateForm(forms.ModelForm):
    message_type = fields.CharField(widget=widgets.Select(choices=[]))

    class Meta:
        model = MessageTemplateModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MessageTemplateForm, self).__init__(*args, **kwargs)
        self.fields["message_type"].widget.choices = [('', '请选择')]
        try:
            dictionary = DataDictionaryModel.objects.get(code_main='message_type')
            self.fields["message_type"].widget.choices += DataDictionaryValueModel.objects.filter(dict_id=dictionary.id).values_list('value', 'title')
        except Exception:
            pass