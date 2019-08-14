# coding:utf-8

from django import forms
from django.utils.translation import ugettext as _

from dictionary.model import DataDictionaryModel, DataDictionaryValueModel
from manager.forms.CommonForm import CommonModelForm
# from system.widgets.JQAdvanceConditionWidget import JQAdvanceConditionWidget


class DataDictionaryForm(CommonModelForm):
    dict_value = forms.fields.CharField(
        # verbose_name=_('Dict Value'),
        required=False,
        widget=forms.widgets.TextInput(attrs={'id': 'dict-simple-value'})  # 自定义属性，生成HTML代码后将有这个属性
    )

    # dict_test = forms.fields.CharField(
    #     required=False,
    #     widget=JQAdvanceConditionWidget(attrs={})
    # )

    class Meta:
        model = DataDictionaryModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DataDictionaryForm, self).__init__(*args, **kwargs)
        self.fields["category"].widget.choices.queryset = self.fields["category"].widget.choices.queryset.exclude(
            status=3)
        cur_dict = self.instance
        if cur_dict:
            # 获取单条value
            related_dict_val_res = DataDictionaryValueModel.objects.filter(dict_id=cur_dict.id).order_by(
                'id')[:1]
            if len(related_dict_val_res) > 0:
                self.__getitem__('dict_value').initial = related_dict_val_res[0].value

        else:
            pass

    def has_changed(self):
        print('has Changed')

    def clean_code_main(self):
        code_main = self.cleaned_data.get('code_main')
        return code_main.lower()

    def clean_code_sub(self):
        code_sub = self.cleaned_data.get('code_sub')
        return code_sub.lower()
