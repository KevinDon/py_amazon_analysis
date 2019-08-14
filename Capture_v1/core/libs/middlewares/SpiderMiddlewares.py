# coding=utf-8
import json
import logging

from core.libs.CommonUnit import getNowTime, getFormatTime, getDifferTime
from core.libs.MongoDbHandler import MongoDB
from core.libs.parts.public import SpiderRequestParts
from core.middlewares import CoreDownloaderMiddleware
from core.models import SyncTaskModel


class BaseSpiderMiddlewares(CoreDownloaderMiddleware):
    """
    爬虫请求/响应处理中间件
    用于在请求中增加请求时间
    用于在响应中增加请求记录的写入
    需要在setting.py中设置启用该Middlewares
    """

    def process_request(self, request, spider):
        """
        请求处理
        :param request:
        :param spider:
        """
        # self.crawler.engine.close_spider(self, 'Spider request counter gt limit by %s ' % self.request_spider_max)
        request.meta.update({'request_at': getNowTime()})
        spider.request_part.request_counter.inc()
        pass

    def process_response(self, request, response, spider):
        """
        响应处理
        :param request:
        :param response:
        :param spider:
        :return:
        """
        # todo 可在此处增加 404 或 500 页面的处理
        spider.request_part.process_request_response(request, response)
        return response

    def process_exception(self, request, exception, spider):
        """
        错误处理
        用于处理请求错误,记录结果信息
        :param request:
        :param exception:
        :param spider:
        """
        spider.request_part.process_request_exception(request, exception)
        return None
        pass


class CaptureHTMLBodyMiddlewares(BaseSpiderMiddlewares):

    def __init__(self):
        super(CaptureHTMLBodyMiddlewares, self).__init__()
        logging.info('爬虫加载CaptureHTMLBody中间件')

    pass


class SyncDataSpiderMiddlewares(BaseSpiderMiddlewares):
    """
    爬虫请求/响应处理中间件
    用于在请求中增加请求时间
    用于在响应中增加请求记录的写入
    需要在setting.py中设置启用该Middlewares
    """

    def __init__(self):
        super(SyncDataSpiderMiddlewares, self).__init__()
        logging.info('爬虫成功加载同步数据处理中间件')

    def process_response(self, request, response, spider):
        """
        响应处理
        :param request:
        :param response:
        :param spider:
        :return:
        """
        # todo 可在此处增加 404 或 500 页面的处理
        super(SyncDataSpiderMiddlewares, self).process_response(request, response, spider)
        try:
            # 检查api接口调用的结果
            response_data = json.loads(response.body)
            if response_data.get('status') == 200:
                sync_task_db = SyncTaskModel()
                # 更新同步任务数据
                sync_task_db.conn.find_one_and_update(
                    filter={'task_code': spider.task_code,'rule_code':spider.rule_code},
                    update={'$set':
                        {
                            'end_page': response_data['tp'],
                            'cur_page': response_data['page'],
                            'total_row': response_data['tr'],
                            'updated_at': getFormatTime(getNowTime())
                        }
                    }
                )
            else:
                spider.logger.error('Post-request %s failed!' % spider.task_api)
                raise Exception('REST API 请求错误')
        except Exception as e:
            spider.logger.error(e)
        finally:
            return response
