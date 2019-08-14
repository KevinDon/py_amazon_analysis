# coding:utf-8

from rest_framework import serializers
from appfront.dv.StatAmazonLineUvItemsConversionRateDv import *


'''按日统计视图'''
class StatAmazonLineUvItemsConversionRateDayDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonLineUvItemsConversionRateDayDv
        fields = "__all__"