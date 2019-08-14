# coding:utf-8

from django.contrib import admin
from appfront.forms.ProductLineForm import *
from django.utils.translation import ugettext as _

from manager.admins import CommonAdmin


@admin.register(ProductLineModel)
class ProductLineAdmin(CommonAdmin):
    list_display = ('title', )
    search_fields = ('title', 'updated_at', 'created_at')
    ordering = ['-created_at']

    show_change_link = True
    form = ProductLineForm
    # Action选项都是在页面上方显示
    actions_on_top = False
    # Action选项都是在页面下方显示
    actions_on_bottom = True
    # 是否显示选择个数
    actions_selection_counter = True

    def has_add_permission(self, request):
        return False