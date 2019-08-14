# coding:utf-8
from django.contrib import admin, messages

from amazon.model import AmazonProductCategoryModel
from appfront.forms.BusinessReportForm import *
from django.utils.translation import ugettext as _
from manager.admin import CommonAdmin
from amazon.forms.AmazonProductCategoryForm import AmazonProductCategoryForm


@admin.register(AmazonProductCategoryModel)
class ProductCategoryAdmin(CommonAdmin):
    form = AmazonProductCategoryForm
    list_display = ('code', 'title', 'level', 'platform',)
    search_fields = ('title', 'platform', 'created_at')
    fieldsets = (
        (None, {
            'fields': ('code', 'title', 'url_alias','parent', 'level', 'platform','na_product_category_list','amazon_keyword_list')
        }),)


