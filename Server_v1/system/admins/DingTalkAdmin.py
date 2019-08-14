from system.model import *
from django.contrib.auth.admin import *
from manager.admin import CommonAdmin


@admin.register(DingTalkModel)
class DingTalkAdmin(CommonAdmin):
    list_display = ('name', 'describe', 'type')
    search_fields = ('name', 'describe', 'type')
    fieldsets = (
        (None, {
            'fields': ('name', 'describe', 'token', 'type')
        }),)

