# coding:utf-8

from django import forms
from django.db.models import Q
from django.utils.translation import ugettext as _
from appfront.model import ProductLineModel


class ProductLineForm(forms.ModelForm):
    class Meta:
        model = ProductLineModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductLineForm, self).__init__(*args, **kwargs)
        _instance = kwargs.get('instance')
        if _instance:
            self.fields["parent"].widget.choices.queryset = self.fields["parent"].widget.choices.queryset.exclude(Q(status=3) | Q(id=_instance.pk))
