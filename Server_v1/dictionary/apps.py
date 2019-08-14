from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DictionaryConfig(AppConfig):
    name = 'dictionary'
    verbose_name = _('Data Dictionary')
