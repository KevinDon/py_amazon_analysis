import logging

from django import forms

from dictionary.model import DataDictionaryModel, DataDictionaryValueModel


class PlatformFormMixin(forms.ModelForm):
    platform = forms.fields.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super(PlatformFormMixin, self).__init__(*args, **kwargs)
        try:
            platform_choice_dict = DataDictionaryModel.objects.filter(code_main='platform', code_sub='choice').first()
            platform_choice = DataDictionaryValueModel.objects.filter(dict_id=platform_choice_dict.id).all()
            self.fields['platform'] = forms.fields.ChoiceField(
                choices=tuple(platform_choice.values_list('value', 'title')))
        except Exception as e:
            self.fields['platform'] = forms.fields.ChoiceField(
                choices=[])
            logging.error(e)


class CommonModelForm(forms.ModelForm):
    default_field_width = None  # 默认field宽度
    require_fields = None  # 设置必填字段

    def __init__(self, *args, **kwargs):
        """
        封装Form表单实例化过程
        :param args:
        :param kwargs:
        """
        # super之前使用base_fields进行修改
        self._set_require_fields()
        super(CommonModelForm, self).__init__(*args, **kwargs)
        # super之后使用instance对象进行修改

    pass

    def _set_require_fields(self):
        """
        根据CommonForm配置的require_fields对字段必填属性进行覆盖
        """
        for field in self.base_fields:
            if self.require_fields and field not in self.require_fields:
                self.base_fields[field].required = False
            else:
                self.base_fields[field].required = True
            if self.default_field_width:
                self.base_fields[field].widget.attrs.update({'style': 'width:%spx' % self.default_field_width})
