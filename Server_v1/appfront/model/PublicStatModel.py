# coding:utf-8

from django.db import models
from django.utils.translation import ugettext as _

class PubStatDaysModel(models.Model):
    yr = models.IntegerField(verbose_name= _('Year'), null=True)
    mo = models.IntegerField(verbose_name= _('Month'), null=True)
    dy = models.IntegerField(verbose_name= _('Day'), null=True)
    date_day = models.DateField(verbose_name=_('Date Day'), null=True)

    def __str__(self):
        return _('Date Day: %s') % self.date_day

    class Meta:
        app_label = "appfront"
        db_table = 'pub_stat_days'
        verbose_name = _('Stat Days')
        verbose_name_plural = _('Stat Days')


class PubStatMonthModel(models.Model):
    yr = models.IntegerField(verbose_name= _('Year'), null=True)
    mo = models.IntegerField(verbose_name= _('Month'), null=True)
    first_day = models.DateField(verbose_name=_('First Day'), null=True)
    last_day = models.DateField(verbose_name=_('Last Day'), null=True)

    def __str__(self):
        return _('First Day: %s') % self.first_day

    class Meta:
        app_label = "appfront"
        db_table = 'pub_stat_month'
        verbose_name = _('Stat Month')
        verbose_name_plural = _('Stat Month')


class PubStatWeeksModel(models.Model):
    yr = models.IntegerField(verbose_name= _('Year'), null=True)
    wk = models.IntegerField(verbose_name= _('Week'), null=True)
    first_day = models.DateField(verbose_name=_('First Day'), null=True)
    last_day = models.DateField(verbose_name=_('Last Day'), null=True)

    def __str__(self):
        return _('First Day: %s') % self.first_day

    class Meta:
        app_label = "appfront"
        db_table = 'pub_stat_weeks'
        verbose_name = _('Stat Week')
        verbose_name_plural = _('Stat Week')