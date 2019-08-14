from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class AppsConfig(AppConfig):
    name = 'appfront'
    verbose_name = _("Business Report")
    main_menu_index = 1