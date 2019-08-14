from dictionary.model import DataDictionaryValueModel
from manager.forms.CommonForm import CommonModelForm


class DataDictionaryValueForm(CommonModelForm):
    class Meta:
        model = DataDictionaryValueModel
        fields = '__all__'
