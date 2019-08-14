import abc
import base64
import json
import urllib.parse
import uuid

from core.libs.CommonUnit import getNowTime
from core.libs.handlers.BaseSpiderHandler import BaseSpiderImplementation
from core.libs.LocalConfigHandler import LocalConfigHandler
from core.libs.items.SpiderItems import ApiSyncSpiderItem
from core.libs.URLHandler import URLHandler
from core.libs.parts.public import SpiderSyncTaskParts


class SyncSpiderHandler(BaseSpiderImplementation):
    task_name = None  # 任务名
    task_resource = None  # 任务资源

    request_end_page = 2

    # 覆盖默认配置,加载数据同步管道
    custom_settings = {
        'ITEM_PIPELINES': {
            'core.libs.pipelines.SpiderPipelines.SyncSystemDataPipeline': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'core.libs.middlewares.SpiderMiddlewares.SyncDataSpiderMiddlewares': 543
        },
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1  # 逐条请求
    }

    load_parts = {
        'task_part': SpiderSyncTaskParts
    }

    def __init__(self, *args, **kwargs):
        self.logger.info(kwargs)
        super(SyncSpiderHandler, self).__init__(*args, **kwargs)
        try:
            # self.request_header = self.rules_analyzer.get_request_header
            # 构造内容处理item
            self.process_item = self.build_process_item()
            # 根据task_name读取本地同步任务和资源配置
            self.config = LocalConfigHandler().config
            # 根据配置获得资源的api
            self.task_api = URLHandler(
                protocol='http',
                host=self.config.get('server', 'host'),
                port=self.config.get('server', 'port'),
                version=self.config.get('server', 'apibaseurl'),
                url_path=self.config.get('resources', self.task_resource)
            ).get_api()

            self.request_end_page = int(self.config.get('sync', 'request_end_page'))
            self.need_base_auth = True
        except Exception as e:
            self.logger.error(e)

    def process_spider_start(self, **kwargs):
        self.logger.info(kwargs)
        # 创建爬虫 job code
        self.job_code = str(uuid.uuid4())
        # 记录开始执行时间
        self.spider_start_at = getNowTime()
        self.auto_load_parts.update(self.load_parts)
        self.load_parts = self.auto_load_parts
        self.process_load_parts(self.load_parts)
        self.process_ready_start(**kwargs)
        # self.process_analysis_rule(rule_xml_str=self.rule)
        self.process_spider_task()
        # self.process_build_capture_item(self.rule_part.get_rule_part('capture'))
        # self.process_build_url_collection(self.rule_part.get_rule_part('urls'), self.rule_part.get_rule_part('task'))
        # self.process_build_url_slices(self.rule_part.get_rule_part('slice'))
        # self.process_build_url_proxy(self.rule_part.get_rule_part('proxy'))
        self.logger.info('爬虫准备完毕,进入同步流程')
        self.spider_start_capture_at = getNowTime()
        pass

    def process_spider_task(self, rule_task_dict=None):
        if rule_task_dict is None:
            rule_task_dict = dict()
        self.task_mode = 2
        super(SyncSpiderHandler, self).process_spider_task(rule_task_dict)
        pass

    def build_process_item(self):
        """
        构造内容项目,用于内容抓取
        :return: process_item
        """
        self.process_item = type('process_item', (ApiSyncSpiderItem,), {})
        return self.process_item()

    def process_parse_item(self, process_item, response):
        return process_item.parse_item(self, response)

    def sync_requests(self, request_url=None):

        if request_url is None:
            request_url = self.task_api

        cur_page = (self.task_part.task.get('cur_page') + 1) if (self.task_part.task.get('end_page') > self.task_part.task.get('cur_page') > 1) else 1
        end_page = min(self.task_part.task.get('end_page'), cur_page - 1 + self.request_end_page)
        self.request_header = self.process_build_request_header(self.rule_part.get_rule_part('requests'), is_ajax=True, authorization=b'Basic ' + base64.b64encode(str('%s:%s' % ('admin', 'admin')).encode()))

        try:
            while cur_page <= end_page:
                yield self.start_request(
                    method='POST',
                    url='?'.join((request_url, urllib.parse.urlencode({'page': cur_page}))),
                    # url=url,
                    body=json.dumps({'pager': {'size': self.config.get('sync', 'size'), 'page': cur_page}, "order": ["-id"]}),
                    callback=self.parse,
                )
                cur_page += 1
        except Exception as e:
            import traceback;
            traceback.print_exc();
            self.logger.error(e)

        @abc.abstractmethod
        def start_requests(self):
            pass

        @abc.abstractmethod
        def parse(self, response):
            pass

        @abc.abstractmethod
        def handles_request(cls, request):
            pass
