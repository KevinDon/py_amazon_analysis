from rest_framework import generics, permissions, viewsets
from rest_framework.authentication import  BasicAuthentication
from rest_framework.exceptions import APIException
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning

from amazon.model import AmazonProductCategoryModel
from api.vo.StatAmazonLineVo import *
from core.libs import QueryFilter as QF
from rest_framework.settings import api_settings
from api.view.authentication import PubAuthentication


class StatAmazonCategoryListSet(APIView):
    versioning_class = URLPathVersioning
    authentication_classes = (BasicAuthentication,)

    def post(self, request, *args, **kwargs):
        request.versioning_scheme.reverse('statamazoncategorylistset', request=request)
        qf = QF()
        try:
            result = qf.parseRequestToFilter(request, AmazonProductCategoryModel, StatAmazonLineVo)
            return Response(result)
        except APIException as e:
            print(e)
            return Response(qf.unsuccessful())


class StatAmazonCategorySet(StatAmazonCategoryListSet):
    versioning_class = URLPathVersioning
    authentication_classes = (PubAuthentication,)