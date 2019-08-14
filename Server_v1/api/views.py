from api.view import *
from api.exceptions import *
import logging
import json


def api_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    # response = exception_handler(exc, context)
    # business error and write log
    # if issubclass(exc.__class__, BusinessException):
    #     logger = logging.getLogger('collect')
    #     log_json = {
    #         'code': exc.__class__.__name__,
    #         'message': getattr(exc, 'message', ''),
    #     }
    #     logger.info(log_json)
    logger = logging.getLogger('collect')
    logger.info(exc)
    qf = QF()
    # Now add the HTTP status code to the response.
    return Response(qf.unsuccessful(msg=exc.default_code, status=exc.status_code))
