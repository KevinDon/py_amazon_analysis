from rule.model import CaptureRuleUserAgentModel
from manager.forms.CommonForm import CommonModelForm


class CaptureRuleUserAgentForm(CommonModelForm):
    class Meta:
        model = CaptureRuleUserAgentModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CaptureRuleUserAgentForm, self).__init__(*args, **kwargs)
        pass
