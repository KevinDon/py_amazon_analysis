from rule.model import CaptureRuleModel
from manager.forms.CommonForm import CommonModelForm


class CaptureRuleForm(CommonModelForm):
    require_fields = ('title', 'scrapy_server')

    class Meta:
        model = CaptureRuleModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CaptureRuleForm, self).__init__(*args, **kwargs)
