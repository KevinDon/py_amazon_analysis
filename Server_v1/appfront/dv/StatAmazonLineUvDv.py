# coding:utf-8

from django.db import models

from django.utils.translation import ugettext as _


'''按Line统计的每天视图数据'''
class StatAmazonLineUvDayDv(models.Model):
    line_id = models.IntegerField(verbose_name= _('Line_ID'), null=True)
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    dy = models.DateField(verbose_name=_('Day'), null=True)
    num = models.IntegerField(verbose_name=_('Count'), null=True)

    def __str__(self):
        return _('Line: %s') % self.title

    class Meta:
        app_label = "appfront"
        managed = False
        db_table = 'view_i_amazon_line_uv_day'
        ordering = ['line_id']
        verbose_name_plural = _('Line U/V for days')


'''按Line统计的每月视图数据'''
class StatAmazonLineUvMonthDv(models.Model):
    line_id = models.IntegerField(verbose_name= _('Line_ID'), null=True)
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    yr = models.IntegerField(verbose_name=_('Year'), null=True)
    mo = models.IntegerField(verbose_name=_('Month'), null=True)
    first_day = models.DateField(verbose_name=_('First Day'), null=True)
    last_day = models.DateField(verbose_name=_('Last Day'), null=True)
    num = models.IntegerField(verbose_name=_('Count'), null=True)

    def __str__(self):
        return _('Line: %s') % self.title

    class Meta:
        app_label = "appfront"
        managed = False
        db_table = 'view_i_amazon_line_uv_month'
        ordering = ['line_id']
        verbose_name_plural = _('Line U/V for months')


'''按Line统计的每周视图数据'''
class StatAmazonLineUvWeekDv(models.Model):
    line_id = models.IntegerField(verbose_name= _('Line_ID'), null=True)
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    yr = models.IntegerField(verbose_name=_('Year'), null=True)
    wk = models.IntegerField(verbose_name=_('Week'), null=True)
    first_day = models.DateField(verbose_name=_('First Day'), null=True)
    last_day = models.DateField(verbose_name=_('Last Day'), null=True)
    num = models.IntegerField(verbose_name=_('Count'), null=True)

    def __str__(self):
        return _('Line: %s') % self.title

    class Meta:
        app_label = "appfront"
        managed = False
        db_table = 'view_i_amazon_line_uv_week'
        ordering = ['line_id']
        verbose_name_plural = _('Line U/V for weeks')
