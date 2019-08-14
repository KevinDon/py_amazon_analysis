from __future__ import unicode_literals
from rest_framework.exceptions import *
from django.utils.translation import ugettext_lazy as _


class ErrorServiceUnavailable(APIException):
    status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    default_detail = _('ERROR SERVICE UNAVAILABLE')
    default_code = 'error_service_unavailable'
