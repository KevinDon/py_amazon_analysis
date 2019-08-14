from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import APIException
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning

from api.vo import StatAmazonVariantVo
from core.libs import QueryFilter as QF
from system.model import TemplateVarModel


class StatAmazonVariantListSet(APIView):
    versioning_class = URLPathVersioning
    authentication_classes = (BasicAuthentication,)

    def post(self, request, *args, **kwargs):
        request.versioning_scheme.reverse('statamazonvariantlistset', request=request)
        qf = QF()
        try:
            result = qf.parseRequestToFilter(request, TemplateVarModel, StatAmazonVariantVo)
            return Response(result)
        except APIException as e:
            print(e)
            return Response(qf.unsuccessful())
