from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from manager.model import TokenModel as Token
from system.model import ApiUserLogModel as ApiLog
from rest_framework.response import Response
from django.contrib.auth import authenticate
from core.libs import QueryFilter as QF
from api.vo import *
from django.utils.translation import ugettext_lazy as _
from api.exceptions import *


class LoginSet(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')
        qf = QF()
        if user is None:
            msg = _('Unable to log in with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')
        else:
            token, created = Token.objects.get_or_create(user=user)
            if not created:
                token.key = token.generate_key()
                Token.objects.filter(user_id=user.id).update(key=token.key)
            log = ApiLog(title="用户登录", content='用户登录成功：'+user.username, action=request.get_full_path(), ip=request.META['REMOTE_ADDR'], creator_id=user.id)
            log.save()
            return Response(qf.successful({'token': token.key}))


class UserProfileSet(APIView):
    def post(self, request, *args, **kwargs):
        auth = request.META.get('HTTP_AUTHORIZATION', b'').split()
        qf = QF()
        try:
            token = Token.objects.get(key=auth[1])
            profile = UserProfileModel.objects.get(user=token.user)
        except (UserProfileModel.DoesNotExist, Token.DoesNotExist):
            profile = UserProfileModel()
            profile.user = token.user
        vo = UserProfileVo(instance=profile)
        if token is None:
            return Response(qf.unsuccessful())
        else:
            return Response(qf.successful(data=vo.data))