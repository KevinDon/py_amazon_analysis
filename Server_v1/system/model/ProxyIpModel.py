from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from manager.model.CommonModel import CommonModel, PlatformMixin
from system.model.IpStatisticsModel import IpStatisticsModel
from system.model.RegionModel import RegionModel


class ProxyIpModel(CommonModel, PlatformMixin):
    AGENT_TYPE = (1, _('Https')), (2, _('Http')), (3, _('Other'))
    TEST_RESULT = (0, _('No Test')), (1, _('Test OK')), (2, _('Test Error'))
    proxy_ip = models.CharField(verbose_name=_('Proxy Ip'), max_length=15, null=True)
    proxy_port = models.CharField(verbose_name=_('Proxy Port'), max_length=6, null=True)
    country = models.CharField(verbose_name=_('Country'), max_length=100, null=True, blank=True)
    region = models.CharField(verbose_name=_('Region'), max_length=100, null=True, blank=True)
    city = models.CharField(verbose_name=_('City'), max_length=100, null=True, blank=True)
    region_code = models.CharField(verbose_name=_('Region Code'), max_length=100, null=True)
    agent_type = models.IntegerField(choices=AGENT_TYPE, verbose_name=_('Agent Type'), default=1, null=True)
    ip_statistics = models.OneToOneField(IpStatisticsModel, on_delete=models.CASCADE, verbose_name=_('Ip Statistics'))
    priority = models.IntegerField(default=0, verbose_name=_('Priority'), null=True)
    test_result = models.IntegerField(choices=TEST_RESULT, verbose_name=_('Test Result'), default=0, null=True)

    def used_times(self):
        return self.ip_statistics.used_times

    def failed_times(self):
        return self.ip_statistics.failed_times

    def last_run_at(self):
        return self.ip_statistics.last_run_at

    def __str__(self):
        return self.proxy_ip

    class Meta:
        app_label = "system"
        db_table = 'system_proxy_ip'
        verbose_name = _("Proxy Ip")
        verbose_name_plural = _("Proxy Ip")


