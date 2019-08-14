# coding:utf-8

from django import forms
from cronjob.model import CronjobJobStoreModel
from django.utils.translation import ugettext as _

class CronjobJobStoreForm(forms.ModelForm):

    class Meta:
        model = CronjobJobStoreModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CronjobJobStoreForm, self).__init__(*args, **kwargs)


