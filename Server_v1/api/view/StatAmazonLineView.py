from rest_framework import generics, permissions, viewsets
from rest_framework.exceptions import APIException
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning

from api.vo.StatAmazonLineVo import *
from core.libs import QueryFilter as QF


class StatAmazonLineSet(APIView):
    versioning_class = URLPathVersioning

    def post(self, request, *args, **kwargs):
        request.versioning_scheme.reverse('statamazonline', request=request)
        qf = QF()
        try:
            result = qf.parseRequestToFilter(request, ProductLineModel, StatAmazonLineVo)
            return Response(result)
        except APIException as e:
            print(e)
            return Response(qf.unsuccessful())
