from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import *
from manager.model.CommonModel import CommonModel
PERMISSION_TYPE = (0, _('Operation')), (1, _('Data'))


class ApiPermissionModel(CommonModel):
    permission = models.OneToOneField(Permission, on_delete=models.CASCADE, related_name='api_permission')
    type = models.IntegerField(choices=PERMISSION_TYPE, default=1,
                               verbose_name=_('Type'), null=True)

    def __str__(self):
        return self.permission.name

    class Meta:
        app_label = "manager"
        verbose_name = _("Permission Type")
        verbose_name_plural = _("Permission Type")
        db_table = 'auth_api_permission'
