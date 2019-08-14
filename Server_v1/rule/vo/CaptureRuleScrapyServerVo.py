from rest_framework import serializers

from system.model import ServerConfigModel


class CaptureRuleScrapyServerVo(serializers.ModelSerializer):
    
    scrapy_server = serializers.SerializerMethodField()

    class Meta:
        model = ServerConfigModel
        fields = '__all__'
        depth = 1

    def get_scrapy_server(self,obj):
        return '%s:%s' % (obj.ip, obj.port)
