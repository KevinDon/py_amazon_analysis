# coding:utf-8
from manager.forms import DepartmentForm
from manager.model import *
from django.contrib.auth.admin import *
from manager.model.DepartmentModel import DepartmentModel
from django.utils.translation import ugettext_lazy as _
from manager.admins.CommonAdmin import *


@admin.register(DepartmentModel)
class DepartmentAdmin(CommonAdmin):
    list_display = ('name', 'code', 'parent_name')
    search_fields = ('name', 'code',)
    fieldsets = (
        (None, {
            'fields': ('name', 'code', 'level', 'parent', 'leaf')
        }),)
    form = DepartmentForm

    def parent_name(self, obj):
        parent_name = '-'
        if obj.parent is not None:
            parent_name = obj.parent.name
        return parent_name
    parent_name.short_description = _('parent name')


