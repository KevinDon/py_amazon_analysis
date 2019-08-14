from rest_framework import generics, permissions, viewsets
from rest_framework.exceptions import APIException
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning

from api.vo import *
from core.libs import QueryFilter as QF


class StatAmazonLineUvDaySet(APIView):
    versioning_class = URLPathVersioning

    def post(self, request, *args, **kwargs):
        # 反向生成URL
        request.versioning_scheme.reverse('statamazonlineuvday', request=request)
        qf = QF()
        try:
            result = qf.parseRequestToFilter(request, StatAmazonLineUvDayDv, StatAmazonLineUvDayDvVo)
            return Response(result)
        except APIException as e:
            print(e)
            return Response(qf.unsuccessful())


class StatAmazonLineUvMonthSet(APIView):
    versioning_class = URLPathVersioning
    def post(self, request, *args, **kwargs):
        # 反向生成URL
        request.versioning_scheme.reverse('statamazonlineuvmonth', request=request)

        qf = QF()
        try:
            result = qf.parseRequestToFilter(request, StatAmazonLineUvMonthDv, StatAmazonLineUvMonthDvVo)
            return Response(result)
        except APIException as e:
            print(e)
            return Response(qf.unsuccessful())



class StatAmazonLineUvWeekSet(APIView):
    versioning_class = URLPathVersioning
    def post(self, request, *args, **kwargs):

        # 反向生成URL
        request.versioning_scheme.reverse('statamazonlineuvweek', request=request)

        qf = QF()
        try:
            result = qf.parseRequestToFilter(request, StatAmazonLineUvWeekDv, StatAmazonLineUvWeekDvVo)
            return Response(result)
        except APIException as e:
            print(e)
            return Response(qf.unsuccessful())