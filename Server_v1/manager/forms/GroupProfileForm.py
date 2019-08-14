# coding:utf-8

from django import forms
from django.utils.translation import ugettext as _
from django.core.handlers.base import logger


class GroupProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(GroupProfileForm, self).__init__(*args, **kwargs)


class GroupInlineForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(GroupInlineForm, self).__init__(*args, **kwargs)
        self.fields["parent"].widget.choices.queryset = self.fields["parent"].widget.choices.queryset.exclude(
            status=3)
