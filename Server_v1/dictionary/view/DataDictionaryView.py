import logging

from core.libs.ajax_query_filter import AjaxQueryFilter as AQF
from dictionary.model import DataDictionaryModel, DataDictionaryCategoryModel
from dictionary.vo import DataDictionaryCategoryVo, DataDictionaryVo


def getDictsByCateAjaxView(request):
    """

    :param request:
    """
    aqf = AQF(request)
    try:
        filters = aqf.parse_conditions(aqf.parse_query_params(request, ('title', 'code', 'platform')))
        res_dict_cates = DataDictionaryCategoryModel.objects.filter(filters).all()
        result = DataDictionaryCategoryVo(instance=res_dict_cates, many=True).data
        return aqf.successful(result, msg='Get Dicts By Cate Success')
    except Exception as e:
        logging.error(e)
        return aqf.unsuccessful(msg='Get Dicts By Cate Failed')


def getDictByCodeAjaxView(request):
    """
    根据code_main和code_sub获取Dictionary
    :type request: object
    :return: JsonResponse
    """
    aqf = AQF(request)
    try:
        filters = aqf.parse_conditions(aqf.parse_query_params(request, ('code_main', 'code_sub')))
        res_dicts = DataDictionaryModel.objects.filter(filters).all()
        result = DataDictionaryVo(instance=res_dicts, many=True).data
        return aqf.successful(result, msg='Get Dict By Code Success')
    except Exception as e:
        logging.error(e)
        return aqf.unsuccessful(msg='Get Dict By Code Failed')


def getDictsByCodeAjaxView(request):
    """
    根据code_main获取同一级别的数据字典和值
    :param request:
    :return:
    """
    aqf = AQF(request)
    try:
        filters = aqf.parse_conditions(aqf.parse_query_params(request, ('code_main',)))
        res_dict = DataDictionaryModel.objects.filter(filters).all()
        result = DataDictionaryVo(instance=res_dict, many=True).data
        return aqf.successful(result, msg='Get Dicts By Code Success')
    except Exception as e:
        logging.error(e)
        return aqf.unsuccessful(msg='Get Dicts By Code Failed')


def getDictsAllAjaxView(request):
    """
    获取全部Dictionary(结构树)
    :param request:
    :return:
    """
    aqf = AQF(request)
    try:
        # params = aqf.parse_query_params(request, ())
        filters = aqf.parse_conditions(aqf.parse_query_params(request, ()))
        res_dict = DataDictionaryModel.objects.filter(filters).all()
        result = DataDictionaryVo(instance=res_dict, many=True).data
        return aqf.successful(result, msg='Get All Dicts Success')
    except Exception as e:
        logging.error(e)
        return aqf.unsuccessful(msg='Get All Dicts Failed')

#
# class DictionaryByCodeGetAPIView(CommonAjaxAPIView):
#     schema = AutoSchema(
#         manual_fields=[
#             coreapi.Field(name='code_main', required=True, description='数据字典主Code', type='string'),
#             coreapi.Field(name='code_sub', required=True, description='数据字典从Code', type='string')
#         ]
#     )
#
#     def get(self, request, *args, **kwargs):
#         try:
#             result = DictionaryByCodeGet(request)
#             return self.response_json(data=result)
#         except Exception as e:
#             logging.error(e)
#
#
# class GetDictsByCodeView(CommonAjaxAPIView):
#     schema = AutoSchema(
#         manual_fields=[
#             coreapi.Field(name='code_main', required=True, description='数据字典主Code', type='string'),
#         ]
#     )
#
#     def get(self, request, *args, **kwargs):
#         try:
#             from system.views import DictionarysByCodeMainGet
#             result = DictionarysByCodeMainGet(request)
#             return self.response_json(data=result)
#         except Exception as e:
#             logging.error(e)
#
#
# class GetAllDictsView(CommonAjaxAPIView):
#     # schema = AutoSchema(
#     #     manual_fields=[]
#     # )
#     schema = AutoSchema()
#
#     def get(self, request, *args, **kwargs):
#         try:
#             from system.views import DictionaryAllGet
#             result = DictionaryAllGet(request)
#             return self.response_json(data=result)
#         except Exception as e:
#             logging.error(e)
