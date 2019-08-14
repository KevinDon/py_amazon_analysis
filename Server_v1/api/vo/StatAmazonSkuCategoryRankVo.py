# coding:utf-8

from rest_framework import serializers
from amazon.dv.StatAmazonSkuCategoryRankDv import *


'''按日统计视图'''
class StatAmazonSkuCategoryRankDayDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonSkuCategoryRankDayDv
        fields = "__all__"


'''按月统计视图'''
class StatAmazonSkuCategoryRankMonthDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonSkuCategoryRankMonthDv
        fields = "__all__"

'''按周统计视图'''
class StatAmazonSkuCategoryRankWeekDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonSkuCategoryRankWeekDv
        fields = "__all__"