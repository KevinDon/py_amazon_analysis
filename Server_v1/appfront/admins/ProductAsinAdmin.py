# coding:utf-8

from django.contrib import admin

from appfront.forms.ProductAsinForm import *


@admin.register(ProductAsinModel)
class ProductAsinAdmin(admin.ModelAdmin):
    list_display = ('sku', 'asin', 'combine_type','updated_at', 'created_at')
    search_fields = ('sku', 'asin', 'combine_type','updated_at', 'created_at')
    readonly_fields = ('updated_at', 'created_at',)
    list_filter = ('combine_type',)
    ordering = ['-created_at']
    show_change_link = True
    form = ProductAsinForm
    # Action选项都是在页面上方显示
    actions_on_top = False
    # Action选项都是在页面下方显示
    actions_on_bottom = True
    # 是否显示选择个数
    actions_selection_counter = True

    # def has_add_permission(self, request):
    #     return False
