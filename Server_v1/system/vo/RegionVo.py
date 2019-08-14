from rest_framework import serializers

from system.model import RegionModel

class RegionVo(serializers.ModelSerializer):
    class Meta:
        model = RegionModel
        fields = '__all__'
