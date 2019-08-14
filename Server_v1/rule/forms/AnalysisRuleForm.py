from rule.model import AnalysisRuleModel
from manager.forms.CommonForm import CommonModelForm


class AnalysisRuleForm(CommonModelForm):
    require_fields = ('title',)
    class Meta:
        model = AnalysisRuleModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AnalysisRuleForm, self).__init__(*args, **kwargs)
        pass
