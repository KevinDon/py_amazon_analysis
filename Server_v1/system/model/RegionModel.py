from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from manager.model.CommonModel import CommonModel


class RegionModel(CommonModel):
    country = models.CharField(verbose_name=_('Country'), max_length=100, null=True)
    country_code = models.CharField(verbose_name=_('Country Code'), max_length=50, null=True)
    region = models.CharField(verbose_name=_('Region'), max_length=100, null=True)
    region_code = models.CharField(verbose_name=_('Region Code'), max_length=100, null=True)
    city = models.CharField(verbose_name=_('City'), max_length=100, null=True)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.country, self.region, self.city,)

    class Meta:
        app_label = "system"
        db_table = 'system_region'
        verbose_name = _("Region")
        verbose_name_plural = _("Region")

    def countyGet(request, **kwargs):
        country_list = RegionModel.objects.values('country').distinct()
        ls = [{c['country']:c['country']} for c in country_list]
        return ls

    def regionByCountryGet(request, **kwargs):
        region_list = RegionModel.objects.filter(kwargs.get('filters')).values('region').distinct()
        ls = [{c['region']:c['region']} for c in region_list]
        return ls

    def cityByRegionGet(request, **kwargs):
        city_list = RegionModel.objects.filter(kwargs.get('filters')).values('city').distinct()
        ls = [{c['city']:c['city']} for c in city_list]
        return ls
