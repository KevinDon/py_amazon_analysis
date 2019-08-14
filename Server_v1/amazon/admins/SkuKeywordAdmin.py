# coding:utf-8
import datetime
import hashlib

import qrcode
from django.contrib import admin, messages

from amazon.forms.SkuKeywordForm import SkuKeywordForm
from amazon.model import SkuKeywordModel
from manager.admin import CommonAdmin


@admin.register(SkuKeywordModel)
class SkuKeywordAdmin(CommonAdmin):
    list_display = ('title', 'platform', 'status',)
    search_fields = ('title', 'platform', 'created_at')
    readonly_fields = ('updated_at', 'created_at', 'creator',)
    list_editable = ('status',)
    form = SkuKeywordForm
    fieldsets = (
        (None, {
            'fields': ('title', 'keyword_type', 'platform', 'status', 'sort', 'amazon_category_list')
        }),)
