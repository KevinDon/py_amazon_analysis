# coding:utf-8
import datetime
import hashlib

import qrcode
from django.contrib import admin, messages

from appfront.forms.BusinessReportForm import *
from django.utils.translation import ugettext as _

from core.constants import MEDIA_ROOT


@admin.register(BusinessReportModel)
class BusinessReportAdmin(admin.ModelAdmin):
    list_display = ('asin_parent', 'asin_child', 'title', 'sessions', 'sessions_percentage', 'page_view', 'page_view_percentage', 'buy_box_percentage', 'units_ordered', 'unit_session_percentage', 'ordered_product_sales', 'total_order_items', 'report_date', 'created_at')
    search_fields = ('asin_parent', 'asin_child','title','report_date','created_at')
    readonly_fields = ('created_at', )
    ordering = ['-created_at']
    show_change_link = True
    form = BusinessReportForm
    # Action选项都是在页面上方显示
    actions_on_top = False
    # Action选项都是在页面下方显示
    actions_on_bottom = True
    # 是否显示选择个数
    actions_selection_counter = True

    def has_add_permission(self, request):
        return False
