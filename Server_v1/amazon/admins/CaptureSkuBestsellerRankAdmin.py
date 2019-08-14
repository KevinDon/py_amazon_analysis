# coding:utf-8
import datetime
import hashlib

import qrcode
from django.contrib import admin, messages
from amazon.model import CaptureSkuBestsellerRankModel
from django.utils.translation import ugettext as _
from manager.admin import CommonAdmin


@admin.register(CaptureSkuBestsellerRankModel)
class CaptureSkuBestsellerRankAdmin(CommonAdmin):
    list_display = ('sku', 'asin', 'category', 'rank_on', 'rank_page', 'platform', 'capture_at')
    search_fields = ('sku', 'asin', 'category', 'capture_at',)
    list_filter = ('platform', 'category_title',)
    readonly_fields = ('sku', 'asin', 'category', 'category_title', 'rank_on', 'rank_page', 'platform', 'capture_at', 'sort', 'status')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def change_view(self, request, object_id, extra_context=None):
        extra_context = extra_context or {}
        extra_context['readonly'] = True
        extra_context['show_save'] = False
        extra_context['show_save_and_continue'] = False
        return super(CaptureSkuBestsellerRankAdmin, self).change_view(request, object_id, extra_context=extra_context)