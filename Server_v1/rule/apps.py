from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class CaptureMasterConfig(AppConfig):
    name = 'rule'
    verbose_name = _("Capture Master")
    verbose_name_plural = _("Capture Master")