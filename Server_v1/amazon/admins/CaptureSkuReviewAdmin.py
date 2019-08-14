# coding:utf-8
import datetime
import hashlib

import qrcode
from django.contrib import admin, messages
from amazon.model import CaptureSkuReviewModel
from django.utils.translation import ugettext as _
from manager.admin import CommonAdmin


@admin.register(CaptureSkuReviewModel)
class CaptureSkuReviewAdmin(CommonAdmin):
    list_display = ('sku', 'asin', 'review_rank', 'author', 'title', 'review_at', 'platform', 'capture_at')
    search_fields = ('sku', 'asin', 'title', 'capture_at',)
    readonly_fields = ('sku', 'asin', 'review_rank', 'review_id', 'author', 'title', 'review_at', 'content', 'selection', 'link', 'platform', 'capture_at', 'sort', 'status')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def change_view(self, request, object_id, extra_context=None):
        extra_context = extra_context or {}
        extra_context['readonly'] = True
        extra_context['show_save'] = False
        extra_context['show_save_and_continue'] = False
        return super(CaptureSkuReviewAdmin, self).change_view(request, object_id, extra_context=extra_context)