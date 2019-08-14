from manager.dv import UserProfileDv
from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseManager(models.Manager):
    def get_queryset(self):
        return self._queryset_class(model=self.model, using=self._db, hints=self._hints)


class CommonModel(models.Model):
    """ Common Abstract Model """
    # STATUS = (0, _('Draft')), (1, _('Enabled')), (2, _('Disabled')), (3, _('Deleted'))
    STATUS = (1, _('Enabled')), (2, _('Disabled'))
    created_at = models.DateTimeField(verbose_name=_('Created At'), null=True, auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('Update At'), null=True,auto_now=True)
    # creator = models.ForeignKey(UserProfileDv, on_delete=models.CASCADE,related_name='creator+', editable=False, null=True, verbose_name=_('Creator'))
    creator_id = models.IntegerField(null=True, editable=False, verbose_name=_('Creator'))
    status = models.IntegerField(choices=STATUS, default=1, verbose_name=_('Status'), null=True)
    sort = models.IntegerField(default=0, verbose_name=_('Sort'), null=True)

    objects = BaseManager()

    def creator(self):
        if self.creator_id is not None:
            return UserProfileDv.objects.get(pk=self.creator_id)
        else:
            return None

    class Meta:
        abstract = True


class PlatformMixin(models.Model):
    """ Platform Abstract Model """
    platform = models.CharField(max_length=100, verbose_name=_('Platform'), default='amazon')
    platform_id = models.IntegerField(default=0, verbose_name=_('Platform Id'), null=True, editable=False)

    class Meta:
        abstract = True


class PurchaseResourceMixin(models.Model):
    purchase_id = models.CharField(null=True, max_length=200, verbose_name=_('Purchase Item ID'), editable=False)

    class Meta:
        abstract = True


class PurchaseParentResourceMixin(PurchaseResourceMixin):
    purchase_parent_id = models.CharField(null=True, max_length=200, verbose_name=_('Purchase Item Parent ID'), editable=False)

    class Meta:
        abstract = True
