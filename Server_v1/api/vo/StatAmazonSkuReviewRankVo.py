# coding:utf-8

from rest_framework import serializers
from amazon.dv.StatAmazonSkuReviewRankDv import *


'''按日统计视图'''
class StatAmazonSkuReviewRankDayDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonSkuReviewRankDayDv
        fields = "__all__"


'''按月统计视图'''
class StatAmazonSkuReviewRankMonthDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonSkuReviewRankMonthDv
        fields = "__all__"

'''按周统计视图'''
class StatAmazonSkuReviewRankWeekDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonSkuReviewRankWeekDv
        fields = "__all__"