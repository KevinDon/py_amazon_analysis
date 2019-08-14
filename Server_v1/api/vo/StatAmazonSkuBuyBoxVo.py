# coding:utf-8

from rest_framework import serializers
from appfront.dv.StatAmazonSkuBuyBoxDv import *


'''按日统计视图'''
class StatAmazonSkuBuyBoxDayDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonSkuBuyBoxDayDv
        fields = "__all__"
