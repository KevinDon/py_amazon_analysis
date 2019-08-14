# coding:utf-8
from system.model import *
from django.contrib.auth.admin import *
from django.utils.translation import ugettext_lazy as _
from manager.admin import CommonAdmin


@admin.register(ProxyIpLogModel)
class ProxyIpLogAdmin(CommonAdmin):
    list_display = ('proxy_ip', 'proxy_port', 'agent_type', 'call_state',)
    search_fields = ('proxy_ip', 'request_content', 'response_result')
    readonly_fields = ('proxy_ip', 'proxy_port', 'agent_type', 'call_state', 'request_content', 'response_result')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, object_id=None):
        return False

    def change_view(self, request, object_id, extra_context=None):
        extra_context = extra_context or {}
        extra_context['readonly'] = True
        extra_context['show_save'] = False
        extra_context['show_save_and_continue'] = False
        return super(ProxyIpLogAdmin, self).change_view(request, object_id, extra_context=extra_context)
