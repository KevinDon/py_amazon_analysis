from django.contrib.auth.models import *
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from manager.model.CommonModel import CommonModel


class GroupProfileModel(CommonModel):
    group = models.OneToOneField(Group, on_delete=models.CASCADE, related_name='group_profile')
    code = models.CharField(_('Group Code'), max_length=50, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    objects = BaseUserManager()

    def __str__(self):
        return self.group.name

    class Meta:
        app_label = "manager"
        db_table = 'auth_group_profile'
        verbose_name = _("Group Profile")
        verbose_name_plural = _("Group Profile")


class GroupModel(Group):

    class Meta:
        proxy = True
        app_label = "manager"
        verbose_name = _("Group")
        verbose_name_plural = _("Group")


class PermissionModel(Permission):

    class Meta:
        proxy = True
        app_label = "manager"
        verbose_name = _("Permission")
        verbose_name_plural = _("Permission")