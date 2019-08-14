# coding:utf-8

from django.contrib import admin
from django.utils.html import format_html

from cronjob.forms.CronjobLogsForm import *
from django.utils.translation import ugettext as _

@admin.register(CronjobLogsModel)
class CronjobLogsAdmin(admin.ModelAdmin):
    list_display = ('cronjob', 'colored_status', 'task_type', 'process', 'thread', 'date_begin', 'date_end', 'time_long', 'created_at')
    search_fields = ('cronjob', 'created_at')
    readonly_fields = ('cronjob', 'colored_status', 'task_type', 'process', 'thread', 'date_begin', 'date_end', 'time_long', 'created_at', 'content')
    list_filter = ( 'cronjob', 'status', 'task_type', )
    # '''设置可编辑字段'''
    # list_editable = ('status',)
    # date_hierarchy = 'created_at'
    ordering = ['-created_at']

    # form set
    fieldsets = (
        (None, {
            'fields': ('colored_status', 'cronjob', 'task_type', ('process', 'thread'), ('date_begin', 'date_end'), 'time_long', 'content', 'created_at')
        }),
    )

    show_change_link = True
    show_history_link = False
    form = CronjobLogsForm
    # Action选项都是在页面上方显示
    actions_on_top = False
    # Action选项都是在页面下方显示
    actions_on_bottom = True
    # 是否显示选择个数
    actions_selection_counter = True


    def has_add_permission(self, request):
        """ 取消后台添加附件功能 """
        return False

    # def has_module_permission(self, request, obj=None):
    #     """ 取消后台历史附件功能 """
    #     return False


    '''所有字段设置为只读'''
    def change_view(self, request, object_id, extra_context=None):
        extra_context = extra_context or {}
        extra_context['readonly'] = True
        extra_context['show_save'] = False
        extra_context['show_save_and_continue'] = False
        return super(CronjobLogsAdmin, self).change_view(request, object_id, extra_context=extra_context)

