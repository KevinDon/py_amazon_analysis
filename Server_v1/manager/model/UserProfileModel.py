from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from manager.model.CommonModel import CommonModel
from manager.model.DepartmentModel import DepartmentModel


class UserProfileModel(CommonModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    department = models.ForeignKey(DepartmentModel, null=True, on_delete=models.CASCADE, related_name='user_department')
    nick = models.CharField(_('nick'), max_length=60, null=True, blank=True)
    ding_talk_account = models.CharField(_('ding talk account'), max_length=60, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        app_label = "manager"
        db_table = 'auth_user_profile'
        verbose_name = _("User Profile")
        verbose_name_plural = _("User Profile")


class UserModel(User):

    class Meta(User.Meta):
        proxy = True
        app_label = "manager"
