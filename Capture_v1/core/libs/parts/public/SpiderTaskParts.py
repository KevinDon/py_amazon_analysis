# -*- coding: utf-8 -*-
import os

from pymongo import ReturnDocument

from core.libs.CommonUnit import getFormatTime, getNowTime
from core.models.CaptureTaskModel import CaptureTaskModel, SyncTaskModel, CaptureJobModel, SyncJobModel


class SpiderTaskParts(object):
    spider = None  # spider
    task_db = CaptureTaskModel()
    task_job_db = CaptureJobModel()
    task = None
    job = None
    task_mode = None

    def __init__(self, spider):
        self.spider = spider
        spider.task_part = self

    def load_task(self, task_code, rule_code, task_dict={}):
        """
        加载任务
        :param task_dict:
        :param rule_code:
        :param task_code:
        """
        if task_code is None:
            raise Exception('爬虫加载任务必须传入task code')
        _new_task = self.task_db.get_new_row()

        _new_task.update(task_dict)

        # 新任务默认redo为True用于生成urls
        _new_task.update(dict(
            task_code=task_code,
            rule_code=rule_code,
            status=1,
            redo=1,
            created_at=getFormatTime(getNowTime()),
        ))

        # 读取已有任务
        self.task = self.task_db.conn.find_one(filter=dict(
            task_code=task_code,
            rule_code=rule_code,
        ))

        # 创建新任务
        if self.task is None:
            _task_id = self.task_db.conn.insert_one(_new_task).inserted_id
            self.task = self.task_db.conn.find_one(filter={'_id': _task_id})
            self.spider.logger.info('爬虫创建任务 %s ' % self.task.get('_id'))
            pass

        self.spider.logger.info('爬虫加载任务 %s ' % self.task.get('_id'))
        # todo 增加任务重做的流程
        return self.task

    def load_job(self, task_code=None, rule_code=None, job_code=None):

        # 创建job
        new_task_detail = self.task_job_db.get_new_row()
        new_task_detail.update(dict(
            task_code=task_code,
            rule_code=rule_code,
            job_code=job_code,
            status=1,
            created_at=getFormatTime(getNowTime()),
            scrapyd_job_id=os.environ.get('SCRAPY_JOB', 'error'),
        ))

        # 返回job信息
        _job_id = self.task_job_db.conn.insert_one(new_task_detail).inserted_id
        self.job = self.task_job_db.conn.find_one(filter={'_id': _job_id})
        return self.job

    def update_task(self, task_code, task_dict: dict = None):
        """
        更新任务
        :param task_code:
        :param task_dict:
        :return:
        """
        if task_dict is None:
            task_dict = {}
        task_dict.update({'updated_at': getFormatTime(getNowTime()), })
        self.task = self.task_db.conn.find_one_and_update(filter={'task_code': task_code},
                                                          update={'$set': task_dict},
                                                          return_document=ReturnDocument.AFTER)
        return self.task

    def update_job(self, task_code, job_code, job_dict: dict = None):
        if job_dict is None:
            job_dict = {}

        job_dict.update({'updated_at': getFormatTime(getNowTime())})
        self.job = self.task_job_db.conn.find_one_and_update(
            filter=dict(
                task_code=task_code,
                job_code=job_code,
            ), update={
                '$set': job_dict
            },
            return_document=ReturnDocument.AFTER)
        return self.job


class SpiderSyncTaskParts(object):
    spider = None  # spider
    task_db = SyncTaskModel()
    task_job_db = SyncJobModel()
    task = None
    task_mode = None

    def __init__(self, spider):
        self.spider = spider
        spider.task_part = self

    def load_task(self, task_code, rule_code,task_dict={}):
        """
        加载任务
        :param rule_code:
        :param task_code:
        """
        if task_code is None:
            raise Exception('爬虫加载任务必须传入task code')
        new_task = self.task_db.get_new_row()
        new_task.update(dict(task_code=task_code, rule_code=rule_code))
        # 读取已有任务
        self.task = self.task_db.conn.find_one(filter={'task_code': task_code, 'rule_code': rule_code})
        # 创建新任务
        if self.task is None:
            _task_id = self.task_db.conn.insert(new_task)
            self.task = self.task_db.conn.find_one(filter={'_id': _task_id})
            self.spider.logger.info('爬虫创建任务 %s ' % self.task.get('_id'))
        self.spider.logger.info('爬虫加载任务 %s ' % self.task.get('_id'))
        # todo 增加任务重做的流程
        return self.task

    pass

    def update_task(self, task_code, task_dict: dict = None):
        """
        更新任务
        :param task_code:
        :param task_dict:
        :return:
        """
        if task_dict is None:
            task_dict = {}
        task_dict.update({'updated_at': getFormatTime(getNowTime()), })
        self.task = self.task_db.conn.find_one_and_update(filter={'task_code': task_code},
                                                          update={'$set': task_dict},
                                                          return_document=ReturnDocument.AFTER)
        return self.task

    def load_job(self, task_code=None, rule_code=None, job_code=None):

        # 创建job
        new_task_detail = self.task_job_db.get_new_row()
        new_task_detail.update(dict(
            task_code=task_code,
            rule_code=rule_code,
            job_code=job_code,
            status=1,
            created_at=getFormatTime(getNowTime()),
            scrapyd_job_id=os.environ.get('SCRAPY_JOB', 'error'),
        ))

        # 返回job信息
        _job_id = self.task_job_db.conn.insert_one(new_task_detail).inserted_id
        self.job = self.task_job_db.conn.find_one(filter={'_id': _job_id})
        return self.job
