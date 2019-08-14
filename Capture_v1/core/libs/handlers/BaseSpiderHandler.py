import abc
import base64
import logging
import random
import uuid
import zlib
from time import sleep, time

import scrapy
from pymongo import ReturnDocument
from scrapy.loader.processors import TakeFirst, Identity
from scrapy.utils.project import get_project_settings
from scrapy.utils.trackref import live_refs

from core.libs.CommonUnit import getNowTime, getFormatTime
from core.libs.items.SpiderItems import CaptureSpiderItem
from core.libs.parts.public import SpiderTaskParts, SpiderRuleParts, SpiderRequestParts, XMLEtAnalyzer
from core.libs.parts.public.SpiderProxyParts import SpiderProxyParts
from core.libs.parts.public.SpiderUrlParts import SpiderUrlParts


class BaseSpiderInterface(metaclass=abc.ABCMeta):
    name = None

    @abc.abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def process_ready_start(self, *args, **kwargs):
        """
        1.处理启动传参
        :param args:
        :param kwargs:
        :rtype: bool
        """
        return bool

    @abc.abstractmethod
    def process_spider_start(self):
        pass

    @abc.abstractmethod
    def process_analysis_rule(self, rule_xml_str: str = None):
        """
        2.处理分析规则
        :param rule:
        :rtype XMLEtAnalyzer instance
        """
        pass

    @abc.abstractmethod
    def process_spider_task(self, rule_task_dict: dict = ()):
        """
        3.解析任务类型
        :rtype int Spider task mode
        """
        pass

    @abc.abstractmethod
    def process_build_capture_item(self, rule_capture_dict: dict = ()):
        """
        4.生成解析内容项目
        :param rule_capture_dict:
        :rtype item
        """
        pass

    @abc.abstractmethod
    def process_build_url_collection(self, rule_url_dict: dict = ()):
        """
        5.生成请求url集合入库
        :param rule_url_dict:
        """
        pass

    @abc.abstractmethod
    def process_build_url_slices(self, rule_slices_dict: dict = ()):
        """
        6.获取分片后的url集合
        :param rule_slices_dict:
        """
        pass

    @abc.abstractmethod
    def process_build_request_header(self, rule_request_dict, method='GET', need_base_auth=False):
        """
        7.构建请求头
        :param rule_request_dict:
        :param method:
        :param need_base_auth:
        """
        pass

    @abc.abstractmethod
    def process_build_request_body(self):
        """
        8.构建请求数据
        """
        pass

    @abc.abstractmethod
    def process_start_request(self, *args, **kwargs):
        """
        9.发送请求
        :param args:
        :param kwargs:
        """
        pass

    @abc.abstractmethod
    def process_parse_item(self, process_item, response):
        """
        10.处理请求结果
        :param process_item:
        :param response:
        """
        pass


class BaseSpiderImplementation(BaseSpiderInterface,
                               scrapy.Spider):
    """
    基础爬虫
    爬虫功能实现的过程:
    1.处理启动传参
    2.处理分析规则
    3.解析任务类型
    4.生成解析内容项目
    5.生成请求url集合入库
    6.获取分片后的url集合
    7.构建请求头
    8.构建请求数据
    9.发送请求
    10.处理请求结果
    """

    name = None  # 爬虫名
    task_code = None  # 任务编码
    rule_code = None  # 规则编码
    rule = None  # 传入的规则(未解析)
    task_mode = None  # 执行的任务类型  1是capture task 抓取任务 2是sync task 同步任务
    task_urls = None  # 执行url缓存池
    proxy_url = None  # 当前代理
    process_item = None  # 当前处理的item
    request_header = None  # 当前处理的请求头
    job_code = None  # 爬虫内编码
    spider_start_at = None  # 爬虫启动时间
    spider_start_capture_at = None  # 爬虫准备完毕时间
    need_base_auth = False  # 采用Base Auth验证
    slice_lock = False  # 分片锁
    # 爬虫功能配件
    load_parts = {}
    auto_load_parts = {
        'task_part': SpiderTaskParts,
        'rule_part': SpiderRuleParts,
        'url_part': SpiderUrlParts,
        'proxy_part': SpiderProxyParts,
        'request_part': SpiderRequestParts,
    }
    task_part: SpiderTaskParts = None
    rule_part: SpiderRuleParts = None
    url_part: SpiderUrlParts = None
    proxy_part: SpiderProxyParts = None
    request_part: SpiderRequestParts = None

    def __init__(self, *args, **kwargs):
        logging.info('启动爬虫')
        super(BaseSpiderImplementation, self).__init__(*args, **kwargs)
        logging.info(kwargs)
        self.process_spider_start(**kwargs)
        pass

    def process_spider_start(self, **kwargs):
        # 爬虫准备启动数据
        self.process_ready_start(**kwargs)
        # 创建爬虫 job code
        self.job_code = str(uuid.uuid4())
        # 记录开始执行时间
        self.spider_start_at = getNowTime()
        self.auto_load_parts.update(self.load_parts)
        self.load_parts = self.auto_load_parts
        # 爬虫加载组件
        self.process_load_parts(self.load_parts)
        # 爬虫分析规则
        self.process_analysis_rule(rule_xml_str=self.rule)
        # 爬虫处理当前任务数据
        self.process_spider_task(rule_task_dict=self.rule_part.get_rule_part('task'))
        # 生成默认请求头
        self.request_header = self.process_build_request_header(self.rule_part.get_rule_part('requests'))
        # 生成内容item
        self.process_build_capture_item(self.rule_part.get_rule_part('capture'))
        # 生成url集合并入库
        self.process_build_url_collection(self.rule_part.get_rule_part('urls'))
        # 分片获取urls
        self.process_build_url_slices(self.rule_part.get_rule_part('task'))
        # 获取请求代理
        # self.process_build_url_proxy(self.rule_part.get_rule_part('proxy'))
        self.logger.info('爬虫准备完毕,进入抓取流程')
        self.spider_start_capture_at = getNowTime()
        pass

    def process_ready_start(self, **kwargs):
        self.task_code = kwargs.get('task_code')
        self.rule_code = kwargs.get('rule_code')
        self.rule = kwargs.get('rule')
        try:
            if self.task_code is None:
                raise Exception('爬虫启动需要传入 task_code!')
            else:
                self.logger.info(msg='爬虫启动采用 task_code 是 %s' % self.task_code)
            if self.rule_code is None:
                raise Exception('爬虫启动需要传入 rule_code!')
            else:
                self.logger.info(msg='爬虫启动采用 rule_code 是 %s' % self.rule_code)
            if self.rule is None:
                raise Exception('爬虫启动需要传入rule!')
            else:
                self.logger.info(msg='爬虫启动采用 rule 是 %s' % self.rule)
            return True
        except Exception as e:
            self.logger.error(e)
            self.crawler.engine.close_spider(self, '爬虫启动失败,原因是 %s ' % e)
            return False

    def process_analysis_rule(self, rule_xml_str: str = None):
        try:
            _rule_xml_str = zlib.decompress(base64.b64decode(rule_xml_str)).decode()
            self.rule_part.load_rule(_rule_xml_str)
        except Exception as e:
            self.logger.error(msg='爬虫分析XML规则失败,因为 %s' % e)
        pass

    def process_spider_task(self, rule_task_dict: dict = None):
        if rule_task_dict is None:
            rule_task_dict = dict()

        self.task_part.task = self.task_part.load_task(self.task_code, self.rule_code, rule_task_dict)
        self.task_part.job = self.task_part.load_job(self.task_code, self.rule_code, self.job_code)

        # scrapy配置映射表

        if rule_task_dict is not None:
            _mapping_settings = {
                # 请求延迟
                'delay': ['DOWNLOAD_DELAY', 'AUTOTHROTTLE_START_DELAY'],
                # 'max-thread': 'CONCURRENT_REQUESTS',
                'max-thread': ['CONCURRENT_REQUESTS', 'CONCURRENT_REQUESTS_PER_DOMAIN', 'AUTOTHROTTLE_TARGET_CONCURRENCY'],
            }
            for _n in _mapping_settings:
                _setting = rule_task_dict.get(_n)
                if rule_task_dict.get(_n) is not None:
                    for s in _mapping_settings[_n]:
                        self.custom_settings[s] = int(_setting)


    def process_build_capture_item(self, rule_capture_dict: dict = {}):
        # 根据rules的capture节点配置生成item过程对象
        item = {i: scrapy.Field(output_processor=TakeFirst() if rule_capture_dict[i]['single'] == '1' else Identity()) for i in rule_capture_dict}
        self.process_item = type('process_item', (CaptureSpiderItem,), item)

    def process_build_url_collection(self, rule_url_dict: dict = ()):
        # todo 配置项值需要迁移到config文件
        _task_redo = 0
        try:
            _task_redo = int(self.task_part.task.get('redo', 0))
        except Exception as e:
            self.logger.error('爬虫获取分片设置错误,原因是%s' % e)

        if _task_redo:
            self.logger.info('爬虫任务为重做模式')
            # 强制重做
            result = self.url_part.build_url_from_rule(rule_url_dict, _task_redo)
            if result:
                self.task_part.task.update(dict(
                    redo=_task_redo,
                    request_total=result,
                    updated_at=getFormatTime(getNowTime())
                ))
            else:
                raise Exception('爬虫批量生成url失败')
        else:
            self.logger.info('爬虫任务为继续模式')
            _remain_url = self.url_part.url_db.conn.find({
                'rule_code': self.rule_code,
                'task_code': self.task_code,
                'status': 1
            }).count()
            if _remain_url < 1:
                self.logger.info('本次爬虫任务已完成,爬虫即将结束')
                raise Exception('本次爬虫任务已完成')

        # url库没有url自动重做
        # if _update_task_data.get('redo') and self.url_part.url_db.conn.find({'rule_code': self.rule_code, 'status': 1}).count() < 1:
        #     _update_task_data.__setitem__('redo', True)
        #     self.logger.info('爬虫上次任务url已请求完毕,即将内部重做')

    def process_build_url_slices(self, rule_task_dict: dict = None):
        # 分片取出url
        if rule_task_dict is None:
            rule_task_dict = dict()
        _task_urls = self.url_part.load_url_by_slice(int(rule_task_dict.get('slice')) or 200)
        if _task_urls:
            # todo 成功生成urls则更新task
            self.task_part.task.update({'request_cursor': int(self.task_part.task.get('request_cursor')) or 0 + len(_task_urls)})
            self.task_part.task_db.conn.find_one_and_update(
                filter={'_id': self.task_part.task.get('_id')},
                update={'$set': self.task_part.task},
                return_document=ReturnDocument.AFTER
            )
        self.task_urls = _task_urls
        return self.task_urls
        pass

    def process_build_url_proxy(self, rule_proxy_dict: dict = None):
        if rule_proxy_dict is None:
            rule_proxy_dict = dict()
        _proxy_type = rule_proxy_dict.get('type', )
        if _proxy_type is None:
            self.proxy_url = None
        else:
            self.proxy_url = self.proxy_part.proxy_selector(int(_proxy_type), rule_proxy_dict)

        return self.proxy_url

    def process_build_request_body(self):
        pass

    def process_start_request(self, *args, **kwargs):
        pass

    def process_build_request_header(self, headers=None, method='GET', is_ajax=False, authorization: str = False, **kwargs):
        """
        构造请求headers
        :param headers:
        :param method:
        :param is_ajax: 是否发起ajax请求
        :type authorization: object
        :return:
        """
        if headers is None:
            headers = {}
        else:
            headers = {str(i).title(): headers[i] for i in headers}
        headers.update({
            'Content-Type': 'application/json' if is_ajax else 'text/html',
            'Accept': 'application/json' if is_ajax else 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        })

        # todo 增强验证内容的处理
        if authorization:
            headers.__setitem__('authorization', authorization)
        return headers

        # if self.need_base_auth:
        #     headers.__setitem__(
        #         'authorization',
        #         b'Basic ' + base64.b64encode(str('%s:%s' % ('admin', 'admin')).encode())
        #     )
        # return headers

    def start_request(self, metas=None, headers=None, *args, **kwargs):
        """
        发起单条请求处理
        :param headers:
        :param metas:
        :param kwargs:
        """
        # 创建task_request_code
        if headers is None:
            headers = {}
        if metas is None:
            metas = {}
        task_request_code = str(uuid.uuid4())
        request_params = kwargs
        # 传入内编请求code
        request_meta = metas
        request_meta.update({'request_code': task_request_code})

        # 使用代理
        self.proxy_url = self.process_build_url_proxy(rule_proxy_dict=self.rule_part.get_rule_part('proxy'))
        if self.proxy_url is not None:
            self.logger.info('采用代理链接 %s' % self.proxy_url)
            request_meta.update({'proxy': self.proxy_url})
            # request_meta.update({'splash': {'args': {'proxy': self.proxy_url}}})
        # 配置请求头
        if self.request_header is not None:
            headers.update(self.request_header)
        else:
            headers = self.process_build_request_header(headers=headers, method=kwargs.get('method', 'GET'))

        request_params.update({
            'meta': request_meta,
            'headers': headers,
            # 'args': {'wait': '0.5'}
        })
        # 增加随机毫秒延迟
        sleep(float('%.2f' % random.random()) / 10)
        return scrapy.Request(**request_params)
        # from scrapy_splash import SplashRequest
        # splash_args = {"lua_source": """
        #                     --splash.response_body_enabled = true
        #                     splash.private_mode_enabled = false
        #                     splash:set_user_agent("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36")
        #                     assert(splash:go("https://item.jd.com/5089239.html"))
        #                     splash:wait(3)
        #                     return {html = splash:html()}
        #                     """}
        # return SplashRequest(**request_params)

    @abc.abstractmethod
    def process_parse_item(self, process_item, response):
        """
        处理内容项目提取
        :param process_item: 内容项目(默认采用的是自身的process_item)
        :param response:
        :return:
        """
        pass

    def save_log(self):
        pass

    def start_requests(self):
        pass

    def parse(self, response):
        pass

    def process_load_parts(self, parts: dict = None):
        """
        加载spider 实例中的parts配置
        :param parts:
        """
        if parts is not None:
            for part in parts:
                self.__setattr__(part, parts[part](self))
        pass
