from rest_framework.authentication import TokenAuthentication
from manager.model import TokenModel as Token
from rest_framework import HTTP_HEADER_ENCODING, exceptions
from django.utils.translation import ugettext_lazy as _
from manager.dv import UserProfileDv


class PubAuthentication(TokenAuthentication):
    keyword = 'Token'
    model = Token
