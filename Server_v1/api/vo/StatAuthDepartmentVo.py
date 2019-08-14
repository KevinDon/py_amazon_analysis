# -*- coding: utf-8 -*-
from rest_framework import serializers

from manager.model.DepartmentModel import DepartmentModel


class StatAuthDepartmentVo(serializers.ModelSerializer):
    
    class Meta:
        model = DepartmentModel
        fields = '__all__'
        depth = 1
