# coding:utf-8

from rest_framework import serializers
from amazon.dv.StatAmazonSkuKeywordRankDv import *


'''按日统计视图'''
class StatAmazonSkuKeywordRankDayDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonSkuKeywordRankDayDv
        fields = "__all__"


'''按月统计视图'''
class StatAmazonSkuKeywordRankMonthDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonSkuKeywordRankMonthDv
        fields = "__all__"

'''按周统计视图'''
class StatAmazonSkuKeywordRankWeekDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonSkuKeywordRankWeekDv
        fields = "__all__"