from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import APIException
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning

from amazon.model import SkuKeywordModel
from api.view import PubAuthentication
from api.vo import StatAmazonKeywordVo
from core.libs import QueryFilter as QF


class StatAmazonKeywordListSet(APIView):
    versioning_class = URLPathVersioning
    authentication_classes = (BasicAuthentication,)

    def post(self, request, *args, **kwargs):
        request.versioning_scheme.reverse('statamazonkeywordlistset', request=request)
        qf = QF()
        try:
            result = qf.parseRequestToFilter(request, SkuKeywordModel, StatAmazonKeywordVo)
            return Response(result)
        except APIException as e:
            print(e)
            return Response(qf.unsuccessful())


class StatAmazonKeywordsSet(StatAmazonKeywordListSet):
    versioning_class = URLPathVersioning
    authentication_classes = (PubAuthentication,)