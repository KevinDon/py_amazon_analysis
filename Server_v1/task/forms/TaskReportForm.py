# coding:utf-8

from cronjob.forms.CronjobForm import CronjobForm

class TaskReportForm(CronjobForm):

    def __init__(self, *args, **kwargs):
        # 设置初始值
        # self.base_fields['task_type'].initial = 2
        super(CronjobForm, self).__init__(*args, **kwargs)
        # 设置初始值
        self.instance.task_type = 5
        self.fields['timezone'].required = False
        self.fields['rule_id'].required = False