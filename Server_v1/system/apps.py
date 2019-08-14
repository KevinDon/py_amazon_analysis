from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SystemConfig(AppConfig):
    name = 'system'
    verbose_name = _("System Configurable")
    verbose_name_plural = _("System Configurable")
