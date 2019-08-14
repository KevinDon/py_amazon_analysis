import logging

from rule.libs.XMLETConstructor import XMLETConstructor
from rule.model import CaptureRuleModel
from rule.vo.CaptureRuleVo import CaptureRuleVo
from core.libs.ajax_query_filter import AjaxQueryFilter as AQF, AQFAuthException


def getCaptureRuleAjaxView(request):
    """
    获取抓取规则
    :param request:
    :return:
    """
    aqf = AQF(request)
    try:
        aqf.need_auth()
        filters = aqf.parse_conditions(aqf.parse_query_params(request, ('id',)))
        res_capture = CaptureRuleModel.objects.filter(filters).all()
        result = CaptureRuleVo(instance=res_capture, many=True).data
        return aqf.successful(result, msg='Get capture rule by capture_type Success')
    except AQFAuthException as ae:
        logging.error(ae)
        return aqf.unsuccessful(msg=str(ae))
    except Exception as e:
        logging.error(e)
        return aqf.unsuccessful(msg='Get capture rule Failed')


def getCaptureRuleXMLAjaxView(request):
    aqf = AQF(request)
    try:
        from appfront.model import ProductAsinModel
        params = aqf.parse_query_params(request, ('id',))
        filters = aqf.parse_conditions(params)
        res_capture = CaptureRuleModel.objects.filter(filters).distinct()
        result = CaptureRuleVo(instance=res_capture, many=True).data
        return aqf.successful( [XMLETConstructor(item).get_xml_format() for item in result], msg='Get capture rule XML success')

    except Exception as e:
        logging.error(e)
        return aqf.unsuccessful(msg='Get captures rule XML Failed')
