# coding:utf-8

from django import forms
from django.utils.translation import ugettext as _


from manager.model import DepartmentModel


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = DepartmentModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DepartmentForm, self).__init__(*args, **kwargs)
        self.fields["parent"].widget.choices.queryset = self.fields["parent"].widget.choices.queryset.exclude(status=3)

