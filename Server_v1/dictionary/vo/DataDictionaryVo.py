from rest_framework import serializers

from dictionary.model import DataDictionaryModel as DictModel
from dictionary.vo.DataDictionaryValueVo import DataDictionaryValueVo


class DataDictionaryVo(serializers.ModelSerializer):
    dict_values = DataDictionaryValueVo(many=True)

    # def to_representation(self, obj):
    #     data = super(DataDictionaryVo, self).to_representation(obj)
    #     data['dict_values'] = DataDictionaryValueModel.objects.can_be_use().filter(dict=data['id']).values_list()
    #     return data

    class Meta:
        model = DictModel
        fields = '__all__'
        depth = 1

    # @staticmethod
    # def DictionaryAllGet(request, **kwargs):
    #     """
    #     获取全部数据字典
    #     :param request: object request
    #     :param kwargs: 传参
    #     :return:
    #     """
    #     # params = request_params(request)
    #
    #     data_dicts = DictModel.objects.filter(FilterMixin.can_be_use()).all()
    #     return data_dicts
    #
    # @staticmethod
    # def DictionaryByCodeGet(request, **kwargs):
    #     """
    #     获取单个数据字典
    #     :param request: request
    #     :param kwargs: 传参 code_main
    #     :return:
    #     :return:
    #     """
    #
    #     data_dict = DictModel.objects.filter(Q(code_main=kwargs.get('code_main__eq')) &
    #                                          Q(code_sub=kwargs.get('code_sub')) &
    #                                          FilterMixin.can_be_use()
    #                                          ).all()
    #     return data_dict
    #
    # @staticmethod
    # def DictionarysByCodeMainGet(request, **kwargs):
    #     """
    #     获取多个数据字典
    #     :param request: request
    #     :param kwargs: 传参
    #     :return:
    #     """
    #     data_dicts = DictModel.objects.filter(Q(code_main=kwargs.get('code_main')) & FilterMixin.can_be_use()).all()
    #     return data_dicts
