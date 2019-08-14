# coding:utf-8

from django.contrib.auth.models import User
from django.db import models
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _


class CronjobModel(models.Model):
    CHOICES_STATUS = ((1, _('Enabled')), (2, _('Disabled')),)
    CHOICES_TYPE = ((1, _('Only once')), (2, _('Repeating')),)
    CHOICES_TIMEZONE = (('Australia/Melbourne', _('Australia/Melbourne')), ('Asia/Shanghai', _('Asia/Shanghai')),)
    CHOICES_COMMANDTYPE = ((1, _('Inner Program')), (2, _('System Shell')), (3, _('System Rule')),)
    CHOICES_TASKTYPE = ((1, _('Capture')), (2, _('Transformation')), (3, _('Analysis')), (4, _('Message')), (5, _('Report')), (9, _('Other')),)

    type = models.IntegerField(verbose_name= _('Type'), choices=CHOICES_TYPE, default=2,)
    code = models.CharField(max_length=50, verbose_name= _('Code'))
    title = models.CharField(max_length=255, verbose_name= _('Title'))
    yr = models.CharField(max_length=100, verbose_name= _('Year'), default='*')
    mo = models.CharField(max_length=255, verbose_name= _('Month'), default='*')
    dy = models.CharField(max_length=255, verbose_name= _('Day'), default='*')
    wk = models.CharField(max_length=255, verbose_name= _('Week'), default='*')
    dy_of_week = models.CharField(max_length=255, verbose_name= _('Day of Week'), default='*')
    hr = models.CharField(max_length=255, verbose_name= _('Hour'), default='*')
    mi = models.CharField(max_length=255, verbose_name= _('Minute'), default='*')
    se = models.CharField(max_length=255, verbose_name= _('Second'), default='*')
    start_date = models.DateTimeField(verbose_name= _('Start Date'), null=True)
    end_date = models.DateTimeField(verbose_name= _('End Date'), null=True)
    timezone = models.CharField(max_length=100, verbose_name= _('Timezone'), null=True, choices=CHOICES_TIMEZONE)
    status = models.IntegerField(verbose_name= _('Status'), choices=CHOICES_STATUS, default=1)
    task_type = models.IntegerField(verbose_name= _('Task Type'), choices=CHOICES_TASKTYPE, default=1)
    command = models.TextField(max_length=5000, verbose_name= _('Command'), null=True)
    rule_id = models.IntegerField(verbose_name=_('Rule ID'), null=True)
    command_type = models.IntegerField(verbose_name= _('Command Type'), null=True, choices=CHOICES_COMMANDTYPE)
    updated_at = models.DateTimeField(verbose_name= _('Update At'), null=True, auto_now=True)
    created_at = models.DateTimeField(verbose_name=_('Created At'), null=True, auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, editable=True, null=True)  # 记录创建该数据的用户

    def __str__(self):
        return _('Job: %s') % self.title

    class Meta:
        app_label = "cronjob"
        db_table = 'na_cronjob'
        verbose_name = _('Cronjob Set')
        verbose_name_plural = _('Cronjob Set')

    def colored_status(self):
        if self.status == 1:
            color_name = 'green'
            _label = self.CHOICES_STATUS[0][1]
        else:
            color_name = 'red'
            _label = self.CHOICES_STATUS[1][1]
        return format_html(
            '<span style="color:{};">{}</span>',
            color_name,
            _label,
        )
    colored_status.short_description = _('Status')

    def colored_type(self):
        if self.type == 1:
            color_name = 'green'
            _label = self.CHOICES_TYPE[0][1]
        else:
            color_name = 'blue'
            _label = self.CHOICES_TYPE[1][1]
        return format_html(
            '<span style="color:{};">{}</span>',
            color_name,
            _label,
        )
    colored_type.short_description = _('Type')
