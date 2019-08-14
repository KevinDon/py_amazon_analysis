from system.model import *
from django.contrib.auth.admin import *
from manager.admin import CommonAdmin


@admin.register(RegionModel)
class RegionAdmin(CommonAdmin):
    list_display = ('city', 'region', 'country',)
    search_fields = ('city', 'region', 'country', 'region_code')
    list_filter = ('country', 'region')
    fieldsets = (
        (None, {
            'fields': ('city', 'region', 'country', 'country_code',)
        }),)
