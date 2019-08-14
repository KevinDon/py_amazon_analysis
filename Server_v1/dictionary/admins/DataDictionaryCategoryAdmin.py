# coding:utf-8

from django.contrib import admin
# from appfront.forms import *
from django.utils.translation import ugettext as _

from dictionary.forms import DataDictionaryCategoryForm
from dictionary.model import DataDictionaryCategoryModel
from manager.admin import CommonAdmin


@admin.register(DataDictionaryCategoryModel)
class DataDictionaryCategoryAdmin(CommonAdmin):
    """ data dictionary admin """
    list_display = ('title','code', 'parent', 'description', 'platform',)
    search_fields = ('title','code','updated_at', 'created_at')
    fieldsets = (
        (None, {
            'fields': ('title', 'code','parent', 'description', 'platform', 'data_type')
        }),)

    form = DataDictionaryCategoryForm

