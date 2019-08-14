# coding:utf-8
import datetime
import hashlib

import qrcode
from django.contrib import admin, messages

from appfront.forms import ProductCategoryForm
from appfront.model import ProductCategoryModel
from appfront.forms.BusinessReportForm import *
from django.utils.translation import ugettext as _
from manager.admin import CommonAdmin


@admin.register(ProductCategoryModel)
class ProductCategoryAdmin(CommonAdmin):

    list_display = ('code', 'title', 'level',)
    search_fields = ('title', 'created_at')
    fieldsets = (
        (None, {
            'fields': ('code', 'title', 'parent', 'level', 'amazon_category','sku_list')
        }),)
    form = ProductCategoryForm


