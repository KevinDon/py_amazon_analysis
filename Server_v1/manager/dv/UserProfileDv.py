# coding:utf-8

from django.db import models

from django.utils.translation import ugettext as _


class UserProfileDv(models.Model):
    id = models.IntegerField(verbose_name=_('Creator Id'), primary_key=True)
    username = models.CharField(max_length=100, verbose_name=_('Username'))
    is_active = models.IntegerField(verbose_name=_('Active'))
    group_id = models.CharField(max_length=100, verbose_name=_('Group Id'))
    group_name = models.CharField(max_length=100, verbose_name=_('Group Name'))
    dep_id = models.CharField(max_length=100, verbose_name=_('Department Id'))
    dep_name = models.CharField(max_length=100, verbose_name=_('Department Name'))
    nick = models.CharField(max_length=100, verbose_name=_('Nick'))
    ding_talk_account = models.CharField(max_length=100, verbose_name=_('Ding Talk Account'))

    def __str__(self):
        return _('%s') % self.username

    class Meta:
        app_label = "manager"
        managed = False
        db_table = 'view_i_auth_user_profile'
        verbose_name_plural = _('User Profile')

