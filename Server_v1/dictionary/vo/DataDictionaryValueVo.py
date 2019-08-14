from rest_framework import serializers

from dictionary.model import DataDictionaryValueModel


class DataDictionaryValueVo(serializers.ModelSerializer):

    class Meta:
        model = DataDictionaryValueModel
        fields = '__all__'

