# coding:utf-8

from django import forms
from django.utils.translation import ugettext as _

from dictionary.model import DataDictionaryCategoryModel
from manager.forms.CommonForm import CommonModelForm


class DataDictionaryCategoryForm(CommonModelForm):
    class Meta:
        model = DataDictionaryCategoryModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DataDictionaryCategoryForm, self).__init__(*args, **kwargs)
        self.fields["parent"].widget.choices.queryset = self.fields["parent"].widget.choices.queryset.exclude(
            status=3)