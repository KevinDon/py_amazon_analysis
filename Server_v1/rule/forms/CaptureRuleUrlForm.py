
from rule.model import CaptureRuleUrlModel
from manager.forms.CommonForm import CommonModelForm


class CaptureRuleUrlForm(CommonModelForm):
    require_fields = ('title', 'host')

    class Meta:
        model = CaptureRuleUrlModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CaptureRuleUrlForm, self).__init__(*args, **kwargs)
