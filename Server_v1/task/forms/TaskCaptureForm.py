# coding:utf-8
from django import forms
from django.utils.translation import ugettext_lazy as _

from cronjob.forms.CronjobForm import CronjobForm
from rule.model import CaptureRuleModel
from task.widgets.TaskWidget import CaptureRuleIdWidget


class TaskCaptureForm(CronjobForm):

    rule_id = forms.IntegerField(widget=CaptureRuleIdWidget(choices=[('', _('Please choose ...'))]))

    def __init__(self, *args, **kwargs):
        # 设置初始值
        self.base_fields['command_type'].initial = 3
        super(CronjobForm, self).__init__(*args, **kwargs)
        # 设置初始值
        self.instance.task_type = 1
        self.fields['timezone'].required = False
        self.fields['rule_id'].required = True

        try:
            self.fields['rule_id'].widget.choices += CaptureRuleModel.objects.filter(status=1).values_list('id', 'title')

        except Exception:
            pass