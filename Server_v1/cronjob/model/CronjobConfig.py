# coding:utf-8
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _

class CronjobConfigModel(models.Model):
    key = models.CharField(verbose_name=_('Key'), max_length=50 )
    name = models.CharField(verbose_name=_('Name'), max_length=100 )
    value = models.CharField(verbose_name=_('Value'), max_length=100 )
    creator = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, null=True)
    updated_at = models.DateTimeField(verbose_name=_('Update At'), null=True, auto_now=True)
    created_at = models.DateTimeField(verbose_name=_('Created At'), null=True, auto_now_add=True)

    def __str__(self):
        return 'KEY: %s' % self.key

    class Meta:
        app_label = "cronjob"
        db_table = 'na_cronjob_job_config'
        ordering = ('key',)
        verbose_name = _('Cronjob Config')
        verbose_name_plural = _('Cronjob Config')

    def __unicode__(self):
        return "key: {}; name: {}; value: {}".format(self.key, self.name, self.value)
