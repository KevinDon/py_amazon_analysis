# coding:utf-8
from system.model import MessageContentModel
from django.conf import settings
from django.contrib import admin, messages
from manager.admin import CommonAdmin


@admin.register(MessageContentModel)
class MessageContentAdmin(CommonAdmin):
    list_display = ('title', 'group_name', 'status', 'message_type', 'created_at', 'updated_at')
    search_fields = ('title', 'created_at')
    list_filter = ('status', )
