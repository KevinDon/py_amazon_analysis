import logging

from django.http import request

from core.libs.ajax_query_filter import AjaxQueryFilter as AQF

from system.model import RegionModel, ProxyIpModel, ServerConfigModel


def getCountryAjaxView(request):
    """
    获取国家列表
    :type request: object
    :return: JsonResponse
    """
    aqf = AQF(request)
    try:
        params = aqf.parse_query_params(request, ())
        filters = aqf.parse_conditions(params)
        result = RegionModel.countyGet(request, filters=filters)
        return aqf.successful(result, msg='Get Country Success')
    except Exception as e:
        logging.error(e)
        return aqf.unsuccessful(msg='Get Country Failed')


def getRegionAjaxView(request):
    """
    根据国家获取地区
    :param request:
    :return:
    """
    aqf = AQF(request)
    try:
        params = aqf.parse_query_params(request, ())
        filters = aqf.parse_conditions(params)
        result = RegionModel.regionByCountryGet(request, filters=filters)
        return aqf.successful(result, msg='Get Region By Country Success')
    except Exception as e:
        logging.error(e)
        return aqf.unsuccessful(msg='Get Region By Country Failed')


def getCityAjaxView(request):
    """
    根据地区获取城市
    :param requset:
    :return:
    """
    aqf = AQF(request)
    try:
        params = aqf.parse_query_params(request, ('region',))
        filters = aqf.parse_conditions(params)
        result = RegionModel.cityByRegionGet(request, filters=filters)
        return aqf.successful(result, msg='Get City By Region Success')
    except Exception as e:
        logging.error(e)
        return aqf.unsuccessful(msg='Get City By Region Failed')


def getIPsAjaxView(request):
    """
    根据地区获取IP
    :param requset:
    :return:
    """
    aqf = AQF(request)
    try:
        server_ip = request.META.get('REMOTE_ADDR', b'')
        auth = request.META.get('HTTP_AUTHORIZATION', b'').split()
        server = ServerConfigModel.objects.get(ip=server_ip, key=auth[1])
        params = aqf.parse_query_params(request, ('country', 'region', 'city',))
        params['test_result'] = 1
        filters = aqf.parse_conditions(params)
        ip_list = ProxyIpModel.objects.exclude(status=3).filter(filters).values('proxy_ip', 'proxy_port', 'country', 'region', 'city', 'agent_type')
        result = []
        if ip_list:
            result = [v for v in ip_list]
        return aqf.successful(result, msg='Get IPs Success')
    except ServerConfigModel.DoesNotExist as e:
        return aqf.unsuccessful(msg='Server DoesNotExist')
    except Exception as e:
        return aqf.unsuccessful(msg='Get IPs Failed')