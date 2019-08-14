from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import APIException
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning

from amazon.model import SkuKeywordModel
from api.vo import StatAmazonProxyIpVo
from core.libs import QueryFilter as QF
from system.model import ProxyIpModel


class StatAmazonProxyIpListSet(APIView):
    versioning_class = URLPathVersioning
    authentication_classes = (BasicAuthentication,)

    def post(self, request, *args, **kwargs):
        request.versioning_scheme.reverse('statamazonproxyiplistset', request=request)
        qf = QF()
        try:
            result = qf.parseRequestToFilter(request, ProxyIpModel, StatAmazonProxyIpVo)
            return Response(result)
        except APIException as e:
            print(e)
            return Response(qf.unsuccessful())
