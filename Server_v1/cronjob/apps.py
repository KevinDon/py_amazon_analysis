from django.apps import AppConfig

from django.utils.translation import ugettext_lazy as _

class CronjobConfig(AppConfig):
    name = 'cronjob'
    verbose_name = _('System Cronjob')
    verbose_name_plural = _("System Cronjobs")
