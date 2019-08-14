# coding:utf-8
from task.forms import TaskTransformationLogsForm
from task.model import *
from django.contrib import admin
from cronjob.admins import CronjobLogsAdmin

from django.utils.translation import ugettext as _


@admin.register(TaskTransformationLogsModel)
class TaskTransformationLogsAdmin(CronjobLogsAdmin):
    list_display = ('cronjob', 'colored_status', 'task_type', 'process', 'thread', 'date_begin', 'date_end', 'time_long', 'created_at')
    list_filter = ('status',)
    form = TaskTransformationLogsForm

    def has_add_permission(self, request):
        """ 取消后台添加附件功能 """
        return False
