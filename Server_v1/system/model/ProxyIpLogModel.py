from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from manager.model.CommonModel import CommonModel, PlatformMixin


class ProxyIpLogModel(CommonModel, PlatformMixin):
    AGENT_TYPE = (1, _('Third')), (2, _('Inner')), (3, _('Other'))
    CALL_STATE = (1, _('Success')), (2, _('Failed'))
    proxy_ip = models.CharField(verbose_name=_('Proxy Ip'), max_length=15, null=True)
    proxy_port = models.CharField(verbose_name=_('Proxy Port'), max_length=6, null=True)
    agent_type = models.IntegerField(choices=AGENT_TYPE, verbose_name=_('Agent Type'), default=1, null=True)
    request_content = models.TextField(max_length=10000, verbose_name=_('Request Content'), null=True)
    response_result = models.TextField(max_length=10000, verbose_name=_('Response Result'), null=True)
    call_state = models.IntegerField(choices=CALL_STATE, verbose_name=_('Call State'), default=1, null=True)

    def __str__(self):
        return self.proxy_ip

    class Meta:
        app_label = "system"
        db_table = 'system_proxy_ip_log'
        verbose_name = _("Proxy Ip Run Log")
        verbose_name_plural = _("Proxy Ip Run Log")


