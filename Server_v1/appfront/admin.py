from django.contrib import admin

# Register your models here.
from appfront.admins import *

from django.utils.translation import ugettext as _

admin.site.site_header = _('Amazon Analysis')
admin.site.site_title = _('Amazon Analysis')