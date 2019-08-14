# coding:utf-8
import datetime
import hashlib

import qrcode
from django.contrib import admin, messages
from amazon.model import CaptureSkuPriceModel
from django.utils.translation import ugettext as _
from manager.admin import CommonAdmin


@admin.register(CaptureSkuPriceModel)
class CaptureSkuPriceAdmin(CommonAdmin):
    list_display = ('sku', 'asin', 'price',  'capture_at')
    search_fields = ('sku', 'asin', 'capture_at',)
    readonly_fields = ('sku', 'asin', 'price', 'link', 'platform', 'capture_at', 'sort', 'status')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def change_view(self, request, object_id, extra_context=None):
        extra_context = extra_context or {}
        extra_context['readonly'] = True
        extra_context['show_save'] = False
        extra_context['show_save_and_continue'] = False
        return super(CaptureSkuPriceAdmin, self).change_view(request, object_id, extra_context=extra_context)