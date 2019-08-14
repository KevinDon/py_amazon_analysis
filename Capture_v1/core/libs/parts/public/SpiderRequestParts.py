from core.libs.CommonUnit import numCounter, getFormatTime, getNowTime, getDifferTime
from core.models.CaptureRequestModel import CaptureRequestModel


class SpiderRequestParts(object):
    spider = None  # spider instance
    request_db = CaptureRequestModel()
    request_counter = numCounter()  # 请求计数器
    request_success_counter = numCounter()  # 成功请求计数器
    request_failed_counter = numCounter()  # 失败请求计数器
    request_spider_max = 10,  # 分片执行最大请求数量

    def __init__(self, spider):
        self.spider = spider
        spider.request_part = self

    def process_request_response(self, request, response):
        try:
            req_item = {
                'url': request.url,
                'method': request.method,
                'cookies': request.cookies,
                'header': {i.decode(): request.headers[i].decode() for i in request.headers},
                'encoding': request.encoding,
                'body': str(request.body),
            }
            res_item = {
                'url': response.url,
                'header': {i.decode(): response.headers[i].decode() for i in response.headers},
                'encoding': response.encoding,
                'body': str(response.body),
            }
            # 记录接收情况
            new_request = self.request_db.get_new_row()
            new_request.update({
                'target_url': response.url,
                'task_code': self.spider.task_code,
                'rule_code': self.spider.rule_code,
                'job_code': self.spider.job_code,
                'request_code': request.meta['request_code'],
                'status': response.status,
                'request_at': getFormatTime(request.meta['request_at']),
                'response_at': getFormatTime(getNowTime()),
                'cost_time': getDifferTime(getNowTime(), request.meta['request_at']),
                'request_data': str(req_item),
                'response_data': str(res_item)
            })
            self.request_db.conn.insert(new_request)
            if response.status == 200:
                self.request_success_counter.inc()
                self.spider.logger.info('爬虫请求是 %s 成功并入库' % request.url)
            else:
                self.spider.logger.error('爬虫请求 %s 失败' % request.url)
                raise Exception('爬虫请求 %s 失败' % request.url)
        except Exception as e:
            self.spider.logger.error(e)

    def process_request_exception(self, request, exception):
        self.request_failed_counter.inc()
        # 请求失败
        try:
            req_item = {
                'url': request.url,
                'method': request.method,
                'cookies': request.cookies,
                'header': {i.decode(): request.headers[i].decode() for i in request.headers},
                'encoding': request.encoding,
                'body': str(request.body),
            }
        except Exception as e:
            req_item = {}

        self.request_db.conn.insert({
            'target_url': request.url,
            'task_code': self.spider.task_code,
            'rule_code': self.spider.rule_code,
            'job_code': self.spider.job_code,
            'request_code': request.meta['request_code'],
            'status': str(exception),
            'request_at': getFormatTime(request.meta['request_at']),
            'response_at': getFormatTime(getNowTime()),
            'cost_time': getDifferTime(getNowTime(), request.meta['request_at']),
            'request': str(req_item),
        })
        self.spider.logger.error('请求异常%s' % exception)
