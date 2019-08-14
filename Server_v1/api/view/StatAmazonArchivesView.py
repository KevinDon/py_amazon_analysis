from rest_framework import generics, permissions, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import APIException
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning

from api.vo.StaAmazonArchivesVo import *
from core.libs import QueryFilter as QF


class StatAmazonSkuSet(APIView):
    versioning_class = URLPathVersioning

    def post(self, request, *args, **kwargs):
        request.versioning_scheme.reverse('statamazonsku', request=request)
        qf = QF()
        try:
            result = qf.parseRequestToFilter(request, ProductAsinModel, StatAmazonSkuVo)
            return Response(result)
        except APIException as e:
            print(e)
            return Response(qf.unsuccessful())


class StatAmazonSkuListGet(APIView):
    versioning_class = URLPathVersioning
    authentication_classes = (BasicAuthentication,)

    def post(self, request, *args, **kwargs):
        request.versioning_scheme.reverse('statamazonsku', request=request)
        qf = QF()
        try:
            result = qf.parseRequestToFilter(request, ProductAsinModel, StatAmazonSkuVo)
            return Response(result)
        except APIException as e:
            print(e)
            return Response(qf.unsuccessful())
