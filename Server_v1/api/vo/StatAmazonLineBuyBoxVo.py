# coding:utf-8

from rest_framework import serializers
from appfront.dv.StatAmazonLineBuyBoxDv import *


'''按日统计视图'''
class StatAmazonLineBuyBoxDayDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonLineBuyBoxDayDv
        fields = "__all__"
