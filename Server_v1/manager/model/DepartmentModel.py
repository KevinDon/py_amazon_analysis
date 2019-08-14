from django.contrib.auth.models import *
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from manager.model.CommonModel import CommonModel


class DepartmentModel(CommonModel):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    code = models.CharField(_('Department Code'), max_length=50, blank=True)
    leaf = models.IntegerField(default=0, verbose_name=_('Leaf'))
    level = models.IntegerField(default=0, verbose_name=_('Level'))
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    purchase_id = models.CharField(null=True, max_length=200, verbose_name=_('Purchase Department Id'))

    def __str__(self):
        return self.name

    class Meta:
        app_label = "manager"
        db_table = 'auth_department'
        verbose_name = _("Department")
        verbose_name_plural = _("Department")
