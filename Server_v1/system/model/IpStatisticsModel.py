from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from manager.model.CommonModel import CommonModel


class IpStatisticsModel(CommonModel):
    used_times = models.IntegerField(verbose_name=_('Proxy Port'), default=0, null=True)
    failed_times = models.IntegerField(verbose_name=_('Proxy Group'), default=0, null=True)
    last_run_at = models.DateTimeField(verbose_name=_('Last Run At'), null=True, auto_now=True)

    def __str__(self):
        return "used_times:{0},failed_times:{1}".format(self.used_times, self.failed_times)

    class Meta:
        app_label = "system"
        db_table = 'system_ip_statistics'
        verbose_name = _("System Ip Statistics")
        verbose_name_plural = _("System Ip Statistics")


