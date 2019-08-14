import binascii
import os
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from manager.model.CommonModel import CommonModel


@python_2_unicode_compatible
class TokenModel(CommonModel):
    """
    The default authorization token model.
    """
    key = models.CharField(_("Key"), max_length=40, primary_key=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='token',
        on_delete=models.CASCADE, verbose_name=_("User")
    )

    class Meta:
        app_label = "manager"
        verbose_name = _("Token")
        verbose_name_plural = _("Tokens")
        db_table = 'auth_token'

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(TokenModel, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key
