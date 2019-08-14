# coding:utf-8
from django.forms import forms

from task.forms import TaskTransformationForm
from task.model import *
from django.contrib import admin
from cronjob.admins import CronjobAdmin
from django.utils.translation import ugettext as _
from task.model.TaskTransformationModel import TaskTransformationListModel


@admin.register(TaskTransformationListModel)
class TaskTransformationListAdmin(CronjobAdmin):
    list_display = ('title', 'code', 'colored_type',  'colored_status', 'command_type', 'updated_at', 'created_at', 'creator', 'data_operations')
    readonly_fields = ('updated_at', 'created_at', 'creator', 'task_type')

    form = TaskTransformationForm

    # def has_add_permission(self, request):
    #     """ 取消后台添加附件功能 """
    #     return False
