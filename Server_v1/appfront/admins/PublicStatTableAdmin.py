# coding:utf-8

from django.contrib import admin
from appfront.forms.PublicStatTableForm import *
from django.utils.translation import ugettext as _

@admin.register(PubStatDaysModel)
class PubStatDaysAdmin(admin.ModelAdmin):
    list_display = ('yr', 'mo', 'dy', 'date_day')
    # search_fields = ('sku', 'asin', 'updated_at','created_at')
    # readonly_fields = ('updated_at', 'created_at', )
    ordering = ['-date_day']

    show_change_link = False
    form = PubStatDaysForm
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
        """ 取消后台删除附件功能 """
        return False

    def save_model(self, request, obj, form, change):
        """ 取消后台编辑附件功能 """
        return False


@admin.register(PubStatMonthModel)
class PubStatMonthAdmin(admin.ModelAdmin):
    list_display = ('yr', 'mo', 'first_day', 'last_day')
    # search_fields = ('sku', 'asin', 'updated_at','created_at')
    # readonly_fields = ('updated_at', 'created_at', )
    ordering = ['-first_day']

    show_change_link = False
    form = PubStatMonthForm
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
        """ 取消后台删除附件功能 """
        return False

    def save_model(self, request, obj, form, change):
        """ 取消后台编辑附件功能 """
        return False


@admin.register(PubStatWeeksModel)
class PubStatWeeksAdmin(admin.ModelAdmin):
    list_display = ('yr', 'wk', 'first_day', 'last_day')
    # search_fields = ('sku', 'asin', 'updated_at','created_at')
    # readonly_fields = ('updated_at', 'created_at', )
    ordering = ['-first_day']

    show_change_link = False
    form = PubStatWeeksForm
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
        """ 取消后台删除附件功能 """
        return False

    def save_model(self, request, obj, form, change):
        """ 取消后台编辑附件功能 """
        return False
