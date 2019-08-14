# coding:utf-8

from django.utils.translation import ugettext_lazy as _
from cronjob.forms.CronjobLogsForm import CronjobLogsForm


class TaskMessageLogsForm(CronjobLogsForm):

    def __init__(self, *args, **kwargs):
        # 设置初始值
        super(TaskMessageLogsForm, self).__init__(*args, **kwargs)
