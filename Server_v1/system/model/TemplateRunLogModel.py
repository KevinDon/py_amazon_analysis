from django.db import models
from django.contrib.auth.models import User
from amazon.model.CaptureSkuBuyBoxStateModel import *
from system.model.MessageTemplateModel import *
from django.utils.translation import ugettext_lazy as _
from manager.model.CommonModel import CommonModel


class TemplateRunLogModel(CommonModel):
    sku_buy_box_state_id = models.IntegerField(null=True, editable=False, verbose_name=_('Buy Box State'))
    template_id = models.IntegerField(null=True, editable=False, verbose_name=_('template'))

    class Meta:
        app_label = "system"
        db_table = 'system_template_run_log'
        verbose_name = _("Template Run Log")
        verbose_name_plural = _("Template Run Log")


