# coding:utf-8

from task.forms import TaskOtherForm
from task.model import *
from django.contrib import admin
from cronjob.admins import CronjobAdmin
from django.utils.translation import ugettext as _


@admin.register(TaskOtherListModel)
class TaskReportListAdmin(CronjobAdmin):
    list_display = ('title', 'code', 'colored_type',  'colored_status', 'command_type', 'updated_at', 'created_at', 'creator', 'data_operations')
    readonly_fields = ('updated_at', 'created_at', 'creator', 'task_type')

    form = TaskOtherForm

    # def has_add_permission(self, request):
    #     """ 取消后台添加附件功能 """
    #     return False
