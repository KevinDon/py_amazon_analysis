from rule.model import CaptureRuleModel, CaptureRuleCookieModel
from manager.forms.CommonForm import CommonModelForm


class CaptureRuleCookieForm(CommonModelForm):
    class Meta:
        model = CaptureRuleCookieModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CaptureRuleCookieForm, self).__init__(*args, **kwargs)
        pass
