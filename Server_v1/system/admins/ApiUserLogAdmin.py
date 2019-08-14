# coding:utf-8
from system.model import *
from django.contrib.auth.admin import *
from django.utils.translation import ugettext_lazy as _
from manager.admin import CommonAdmin


@admin.register(ApiUserLogModel)
class ApiUserLogAdmin(CommonAdmin):
    list_display = ('title', 'content', 'action', 'ip',)
    search_fields = ('title', 'content', 'action')
    readonly_fields = ('title', 'content', 'action', 'ip')

    # def save_model(self, request, obj, form, change):
    #     if obj.creator is None:
    #         obj.creator = request.user
    #     super().save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, object_id=None):
        return False

    def change_view(self, request, object_id, extra_context=None):
        extra_context = extra_context or {}
        extra_context['readonly'] = True
        extra_context['show_save'] = False
        extra_context['show_save_and_continue'] = False
        return super(ApiUserLogAdmin, self).change_view(request, object_id, extra_context=extra_context)
