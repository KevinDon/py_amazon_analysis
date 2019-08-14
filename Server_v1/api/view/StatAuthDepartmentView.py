# -*- coding: utf-8 -*-
import logging

from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning
from rest_framework.views import APIView

from api.vo import StatAuthDepartmentVo
from core.libs import QueryFilter as QF
from manager.model.DepartmentModel import DepartmentModel


class StatAuthDepartmentView(APIView):
    versioning_class = URLPathVersioning
    authentication_classes = (BasicAuthentication,)

    def post(self, request, *args, **kwargs):
        request.versioning_scheme.reverse('statauthdepartment', request=request)
        qf = QF()
        try:
            result = qf.parseRequestToFilter(request, DepartmentModel, StatAuthDepartmentVo)
            return Response(result)
        except APIException as e:
            logging.error(e)
            return Response(qf.unsuccessful())
