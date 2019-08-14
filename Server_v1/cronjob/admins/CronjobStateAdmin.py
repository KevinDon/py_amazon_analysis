# coding:utf-8

from django.contrib import admin
from django.utils.html import format_html

from cronjob.forms.CronjobStateForm import *
from django.utils.translation import ugettext as _

@admin.register(CronjobStateModel)
class CronjobStateAdmin(admin.ModelAdmin):
    list_display = ('cronjob', 'task_type', 'colored_status', 'colored_action', 'created_at')
    search_fields = ('cronjob', 'created_at')
    list_filter = ('status', 'action', 'task_type', )
    # '''设置可编辑字段'''
    # list_editable = ('status',)
    # date_hierarchy = 'created_at'

    readonly_fields = ('cronjob', 'created_at', 'task_type', 'status', 'action')
    ordering = ['-created_at']

    show_change_link = True
    form = CronjobStateForm
    # Action选项都是在页面上方显示
    actions_on_top = False
    # Action选项都是在页面下方显示
    actions_on_bottom = True
    # 是否显示选择个数
    actions_selection_counter = True

    def has_add_permission(self, request):
        """ 取消后台添加附件功能 """
        return False

    '''所有字段设置为只读'''
    def change_view(self, request, object_id, extra_context=None):
        extra_context = extra_context or {}
        extra_context['readonly'] = True
        extra_context['show_save'] = False
        extra_context['show_save_and_continue'] = False
        return super(CronjobStateAdmin, self).change_view(request, object_id, extra_context=extra_context)