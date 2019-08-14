from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from manager.model.CommonModel import CommonModel


class RegionIpModel(CommonModel):
    country = models.CharField(verbose_name=_('Country'), max_length=100, null=True)
    country_code = models.CharField(verbose_name=_('Country Code'), max_length=50, null=True)
    region = models.CharField(verbose_name=_('Region'), max_length=100, null=True)
    region_code = models.CharField(verbose_name=_('Region Code'), max_length=100, null=True)
    city = models.CharField(verbose_name=_('City'), max_length=100, null=True)
    locale = models.CharField(max_length=50, verbose_name=_('Locale'), null=True)
    timezone = models.CharField(max_length=100, verbose_name=_('Timezone'), null=True)
    ip_from = models.BigIntegerField(default=0, verbose_name=_('Ip From'), null=True)
    ip_to = models.BigIntegerField(default=0, verbose_name=_('Ip To'), null=True)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.country, self.region, self.city,)

    class Meta:
        app_label = "system"
        db_table = 'system_region_ip'
        verbose_name = _("Region Ip")
        verbose_name_plural = _("Region Ip")

