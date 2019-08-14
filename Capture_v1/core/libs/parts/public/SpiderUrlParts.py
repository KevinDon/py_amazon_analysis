# -*- coding: utf-8 -*-
import re
import urllib.parse

import pymongo
from pymongo import UpdateOne, ReplaceOne, ReturnDocument

from core.libs.CommonUnit import getFormatTime, getNowTime
from core.libs.LocalConfigHandler import LocalConfigHandler
from core.models import CaptureUrlMode


class SpiderUrlParts(object):
    spider = None  # spider instance
    url_db = CaptureUrlMode()

    def __init__(self, spider):
        self.spider = spider
        spider.url_part = self

    def build_url_from_rule(self, url_rule, is_redo=False):
        # todo 需要迁移url生成到此处
        try:
            _urls_generator = self.spider.rule_part.rule_analyzer.get_all_urls_text
            _urls = list(*_urls_generator)

            self.spider.task_total_url = len(_urls)

            # 分片写库
            _slice_num = 5000
            _slice_save_counter = 0
            _new_url = self.url_db.get_new_row()

            # todo 重构redo
            if is_redo:
                for _slice in range(0, len(_urls), _slice_num):
                    # 任务重做
                    _bulk_list = [UpdateOne(
                        filter=dict(
                            url=_url[1],
                            rule_code=self.spider.rule_code,
                            task_code=self.spider.task_code,
                        ),
                        update={'$set': dict(_new_url, **{
                            'url': _url[1],
                            'rule_code': self.spider.rule_code,
                            'task_code': self.spider.task_code,
                            'job_code': self.spider.job_code,
                            'sort': _url[0] + _slice,
                            'status': 1,
                        }), }, upsert=True) for _url in enumerate(_urls[_slice:_slice + _slice_num])]
                    res = self.url_db.conn.bulk_write(_bulk_list, ordered=False)
                    _slice_save_counter += res.upserted_count
                    _bulk_list.clear()
                self.spider.logger.info('爬虫根据rule生成了 %s 条url并入库' % _slice_save_counter)
                _urls.clear()
                return self.spider.task_total_url
            else:
                self.spider.logger.info('爬虫继续当前任务,不生成新的url')
                return self.spider.task_total_url
        except Exception as e:
            self.spider.logger.info('爬虫批量生成Urls出错,原因 %s' % e)
            return False

    def load_url_by_slice(self, url_slice=20):
        _urls = [self.url_db.conn.find_one_and_update(
            filter=dict(
                rule_code=self.spider.rule_code,
                job_code=self.spider.job_code,
                status=1,
            ),
            update={'$set': dict(
                used_at=getFormatTime(getNowTime()),
                status=2,
            )},
            return_document=ReturnDocument.BEFORE,
            sort=[('sort', pymongo.ASCENDING)]) for i in range(url_slice)]
        _urls = [i for i in _urls if i is not None]
        self.spider.logger.info('爬虫分片成功取出%s条url' % len(_urls))
        return _urls

    def get_all_url_text(self):
        pass
