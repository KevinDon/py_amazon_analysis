# coding:utf-8

from django.contrib import admin
from django.utils.html import format_html

from cronjob.forms.CronjobJobStoreForm import *
from django.utils.translation import ugettext as _

@admin.register(CronjobJobStoreModel)
class CronjobJobStoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'task_type', 'next_run_time', 'updated_at', 'created_at')
    search_fields = ('name', 'updated_at', 'created_at')
    # '''设置可编辑字段'''
    # list_editable = ('status',)
    date_hierarchy = 'next_run_time'

    readonly_fields = ('updated_at', 'created_at', 'task_type')
    ordering = ['-updated_at']

    show_change_link = True
    form = CronjobJobStoreForm
    # Action选项都是在页面上方显示
    actions_on_top = False
    # Action选项都是在页面下方显示
    actions_on_bottom = True
    # 是否显示选择个数
    actions_selection_counter = True

    def has_add_permission(self, request):
        """ 取消后台添加附件功能 """
        return False
