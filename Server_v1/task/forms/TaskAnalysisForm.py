# coding:utf-8
from django import forms
from django.utils.translation import ugettext_lazy as _

from cronjob.forms.CronjobForm import CronjobForm
from cronjob.model import CronjobModel
from rule.model import AnalysisRuleModel
from task.widgets.TaskWidget import AnalysisRuleIdWidget


class TaskAnalysisForm(CronjobForm):

    command_type = forms.IntegerField(widget=forms.Select(choices=tuple([('', _('Please choose ...'))] + list(CronjobModel.CHOICES_COMMANDTYPE))))
    rule_id = forms.IntegerField(widget=AnalysisRuleIdWidget(choices=[('', _('Please choose ...'))]))

    def __init__(self, *args, **kwargs):
        # 设置初始值
        self.base_fields['command_type'].initial = 3
        super(CronjobForm, self).__init__(*args, **kwargs)
        # 设置初始值
        self.instance.task_type = 3
        self.fields['timezone'].required = False
        self.fields['rule_id'].required = True

        try:
            self.fields['rule_id'].widget.choices += AnalysisRuleModel.objects.filter(status=1).values_list('id', 'title')
        except Exception:
            pass
