from system.model import *
from django.contrib.auth.admin import *
from manager.admin import CommonAdmin
from system.forms import *


@admin.register(ProxyIpModel)
class ProxyIpAdmin(CommonAdmin):
    list_display = ('proxy_ip', 'proxy_port',  'city', 'region', 'country',  'agent_type', 'priority', 'test_result',
                    'used_times', 'failed_times', 'last_run_at')
    search_fields = ('proxy_ip', 'proxy_port')
    list_filter = ('agent_type',)
    fieldsets = (
        (None, {
            'fields': ('proxy_ip', 'proxy_port', 'agent_type', 'country',  'region', 'city', 'priority')
        }),)
    form = ProxyIpForm

    def save_model(self, request, obj, form, change):
        if not hasattr(obj, 'ip_statistics'):
            statistics = IpStatisticsModel(used_times=0, failed_times=0)
            statistics.save()
            obj.ip_statistics = statistics
        super().save_model(request, obj, form, change)
