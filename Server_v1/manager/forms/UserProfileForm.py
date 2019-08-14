# coding:utf-8

from django import forms
from django.utils.translation import ugettext as _
from django.core.handlers.base import logger
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import Group


class UserProfileForm(UserChangeForm):
    groups = forms.ModelMultipleChoiceField(Group.objects.all(), widget=forms.widgets.SelectMultiple())

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['groups'].widget.allow_multiple_selected = False


class UserInlineForm(UserChangeForm):

    def __init__(self, *args, **kwargs):
        super(UserInlineForm, self).__init__(*args, **kwargs)
        self.fields["department"].widget.choices.queryset = self.fields["department"].widget.choices.queryset.exclude(
            status=3)
