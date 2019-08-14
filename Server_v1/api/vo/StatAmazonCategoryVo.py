# coding:utf-8

from rest_framework import serializers

from amazon.model import AmazonProductCategoryModel
'''Amazon Product Category 资料'''


class StatAmazonCategoryVo(serializers.ModelSerializer):
    class Meta:
        model = AmazonProductCategoryModel
        fields = "__all__"
