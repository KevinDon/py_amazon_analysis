# coding:utf-8

from rest_framework import serializers

from system.model import TemplateVarModel

''' TemplateVarModel 资料'''


class StatAmazonVariantVo(serializers.ModelSerializer):
    class Meta:
        model = TemplateVarModel
        fields = "__all__"
