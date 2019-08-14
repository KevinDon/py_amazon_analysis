from rest_framework import serializers

from dictionary.model import DataDictionaryCategoryModel
from dictionary.vo.DataDictionaryVo import DataDictionaryVo


class DataDictionaryCategoryVo(serializers.ModelSerializer):
    dicts = DataDictionaryVo(many=True)

    class Meta:
        model = DataDictionaryCategoryModel
        fields = '__all__'
        depth = 2
