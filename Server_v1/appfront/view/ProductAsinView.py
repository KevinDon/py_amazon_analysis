import logging

from core.libs.ajax_query_filter import AjaxQueryFilter as AQF, AQFAuthException


def getProductAjaxView(request):
    aqf = AQF(request)
    try:
        from appfront.model import ProductAsinModel
        filters = aqf.parse_conditions(aqf.parse_query_params(request, ('capture_type',)))
        result = ProductAsinModel.skuGet(request, filters=filters)
        return aqf.successful(result, msg='Get product success')

    except Exception as e:
        logging.error(e)
        return aqf.unsuccessful(msg='Get product Failed')
