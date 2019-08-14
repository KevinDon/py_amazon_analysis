# coding:utf-8

from rest_framework import serializers

from amazon.model import SkuKeywordModel
from appfront.model import ProductLineModel

'''Keyword资料'''


class StatAmazonKeywordVo(serializers.ModelSerializer):
    class Meta:
        model = SkuKeywordModel
        fields = "__all__"
