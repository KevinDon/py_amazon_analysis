# coding:utf-8

from rest_framework import serializers
from amazon.dv.StatAmazonSkuBestsellerRankDv import *


'''按日统计视图'''
class StatAmazonSkuBestsellerRankDayDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonSkuBestsellerRankDayDv
        fields = "__all__"


'''按月统计视图'''
class StatAmazonSkuBestsellerRankMonthDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonSkuBestsellerRankMonthDv
        fields = "__all__"

'''按周统计视图'''
class StatAmazonSkuBestsellerRankWeekDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonSkuBestsellerRankWeekDv
        fields = "__all__"