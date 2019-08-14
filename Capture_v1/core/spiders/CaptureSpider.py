# coding:utf-8
import random
import uuid
from time import sleep

import scrapy

from core.libs.handlers.CaptureSpiderHandler import CaptureSpiderHandler


class CaptureSpider(CaptureSpiderHandler):
    name = "CaptureSpider"

    def __init__(self, *args, **kwargs):
        self.slice_lock = True
        super(CaptureSpider, self).__init__(*args, **kwargs)

    '''请求处理'''
    def start_requests(self):
        """
        请求处理
        :rtype: object
        """
        try:
            # 当前爬取任务执行的内置任务池
            _task_poll = self.task_urls
            # 读取任务请求分片数
            _slice = int(self.task_part.task.get('slice', 500))

            while _task_poll:
                # 取出第一条url
                _cur_url = _task_poll[0].get('url')
                del _task_poll[0]
                # 当任务池的数量少于分片数量,从url表中继续加载url
                if len(_task_poll) < _slice and self.slice_lock:
                    self.task_urls = self.process_build_url_slices(rule_task_dict=self.rule_part.get_rule_part('task'))
                    if len(self.task_urls) < _slice:
                        self.slice_lock = False
                    self.logger.info('当分片运行的url还有%s个,增加读取分片url%s' % (len(_task_poll), len(self.task_urls)))
                    _task_poll += self.task_urls
                self.logger.info('当分片运行的url还有%s个' % len(_task_poll))
                self.logger.info('发起请求%s' % _cur_url)

                _request_metas = {}
                # 请求头
                _request_headers = self.process_build_request_header(headers=self.rule_part.get_rule_part('request'))
                # 内部参数
                _request_metas['request_code'] = str(uuid.uuid4())
                # 使用代理
                _proxy_url = self.process_build_url_proxy(rule_proxy_dict=self.rule_part.get_rule_part('proxy'))
                if _proxy_url is not None:
                    self.logger.info('本次爬取采用代理链接 %s' % _proxy_url)
                    _request_metas['proxy'] = _proxy_url
                # 内置等待时间
                sleep(float(self.task_part.task.get('delay', 0)) + float('%.2f' % random.random()) / 10)

                yield scrapy.Request(
                    url=_cur_url,
                    callback=self.parse,
                    headers=_request_headers,
                    meta=_request_metas,
                )

            # for url in self.task_urls:
            #     self.logger.info('发起请求%s' % url)
            #     yield self.start_request(
            #         url=url.get('url', ''),
            #         callback=self.parse,
            #         headers=self.request_header
            #     )

        except Exception as e:
            self.logger.error('Error for Request')

    '''解析结果'''
    def parse(self, response):
        self.logger.info(response.status)
        try:
            yield self.process_parse_item(self.process_item, response)
        except Exception as e:
            import traceback;
            traceback.print_exc();
            self.logger.error('抓取失败,url = %s', response.url)
            self.logger.error(e)

    # Bingo! Here we get the result and You can restore or output it
    def handle_spider_closed(self, spider):
        self.logger.info('结束关闭')
