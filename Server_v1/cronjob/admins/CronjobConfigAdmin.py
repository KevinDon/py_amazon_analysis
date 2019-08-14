# coding:utf-8

from django.contrib import admin
from django.utils.html import format_html

from cronjob.forms.CronjobConfigForm import *
from django.utils.translation import ugettext as _

@admin.register(CronjobConfigModel)
class CronjobConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'creator', 'updated_at', 'created_at')
    search_fields = ('creator', 'created_at')
    list_filter = ('name', 'value', )
    list_editable = ('value', )
    readonly_fields = ('creator', 'created_at', 'updated_at', 'name', 'key')
    ordering = ['-created_at']

    show_change_link = True
    form = CronjobConfigForm
    # Action选项都是在页面上方显示
    actions_on_top = False
    # Action选项都是在页面下方显示
    actions_on_bottom = True
    # 是否显示选择个数
    actions_selection_counter = True

    def has_add_permission(self, request):
        """ 取消后台添加附件功能 """
        return False

    def has_delete_permission(self, request, obj=None):
        return False