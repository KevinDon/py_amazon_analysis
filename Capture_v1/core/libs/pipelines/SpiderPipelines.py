import json
import logging

from pymongo import ReturnDocument

from core.libs.CommonUnit import getNowTime, getFormatTime, getDifferTime
from core.libs.MongoDbHandler import MongoDB
from core.models.CaptureTaskModel import CaptureTaskModel, SyncTaskModel


class MongoPipeline(object):
    """
    Mongo DB 数据管道
    用于处理抓取数据写 Mongo DB
    需要在setting.py中设置启用该pipeline
    """

    def __init__(self):
        pass

    # 可选实现，做参数初始化等
    # doing something

    def process_item(self, item, spider):
        # item (Item 对象) – 被爬取的item
        # spider (Spider 对象) – 爬取该item的spider
        # 这个方法必须实现，每个item pipeline组件都需要调用该方法，
        # 这个方法必须返回一个 Item 对象，被丢弃的item将不会被之后的pipeline组件所处理。
        spider.logger.info('MongoPipeline process item')
        return item

    def open_spider(self, spider):
        # spider (Spider 对象) – 被开启的spider
        # 可选实现，当spider被开启时，这个方法被调用。
        pass

    def close_spider(self, spider):
        # spider (Spider 对象) – 被关闭的spider
        # 可选实现，当spider被关闭时，这个方法被调用
        # todo 记录爬虫运行状态
        pass


class CaptureHTMLBodyPipeline(MongoPipeline):
    """
    数据抓取类型爬虫数据管道
    任务配置的模式(mode)为1
    """

    def open_spider(self, spider):
        # spider (Spider 对象) – 被开启的spider
        # 可选实现，当spider被开启时，这个方法被调用。
        print('Load in CaptureHTMLBodyPipeline')
        # import requests as req
        # url = 'https://oapi.dingtalk.com/robot/send?access_token='
        # req.api.post(url + '9dc23fc9f30248e54bcf36ca66d4cbc664660a51e791d282dbe9f97177c55ae6',
        #              json=json.dumps({"msgtype": 'markdown',
        #                    'markdown': {"title": '爬虫开启', "text": '爬虫任务开启,本次任务rule_code:%s' % spider.rule_code},
        #                    "at": {"isAtAll": True}}))

        # 启动蜘蛛
        # 更新job信息
        spider.logger.info('爬虫已启动')
        pass

    pass

    def close_spider(self, spider):
        # spider (Spider 对象) – 被关闭的spider
        # 可选实现，当spider被关闭时，这个方法被调用
        # import requests as req
        # url = 'https://oapi.dingtalk.com/robot/send?access_token='
        # req.api.post(url + '9dc23fc9f30248e54bcf36ca66d4cbc664660a51e791d282dbe9f97177c55ae6',
        #              json=json.dumps({"msgtype": 'markdown',
        #                    'markdown': {"title": '爬虫完成', "text": '爬虫任务已完成,本次任务rule_code:%s' % spider.rule_code},
        #                    "at": {"isAtAll": True}}))
        spider.logger.info('爬虫已结束')
        _req_counter = 0
        _req_suc_counter = 0
        _req_fai_counter = 0
        try:
            _req_counter = int(spider.request_part.request_counter.counter)
            _req_suc_counter = int(spider.request_part.request_success_counter.counter)
            _req_fai_counter = int(spider.request_part.request_failed_counter.counter)
        except Exception as e:
            spider.logger.error('爬虫请求统计发生错误,%s' % e)

        # 关闭时候,更新job数据
        spider.task_part.task_job_db.conn.find_one_and_update(
            filter=dict(_id=spider.task_part.job.get('_id')),
            update={'$set': dict(
                status=2,
                request_cursor=_req_counter,
                request_total=int(len(spider.task_urls)),
                request_success=_req_suc_counter,
                request_failed=_req_fai_counter,
                finished_at=getFormatTime(getNowTime()),
                cost_time=getDifferTime(getNowTime(), spider.spider_start_at)
            )}
        )
        # 关闭时候,更新task数据
        spider.task_part.task_db.conn.find_one_and_update(
            filter=dict(_id=spider.task_part.task.get('_id')),
            update={'$set': dict(
                # request_total=int(spider.request_part.request_counter.counter) + _req_counter,
                request_success=int(spider.request_part.request_success_counter.counter) + _req_suc_counter,
                request_failed=int(spider.request_part.request_failed_counter.counter) + _req_fai_counter,
                updated_at=getFormatTime(getNowTime()),
            )}
        )
        pass

    def process_item(self, item, spider):
        spider.logger.info('CaptureHTMLBodyPipeline process item')
        capture_html_db = MongoDB('pub_capture_html')
        counters_db = MongoDB('counters')
        insert_item = dict(item)
        _res = counters_db.conn.find_one_and_update(filter={'_id': 'auto_res_id'}, update={'$inc': {'sequence_value': 1}})
        insert_item.update({
            # 'auto_id': int(getNowTime() * 1000),
            'auto_id': int(_res['sequence_value']),
            'capture_ip': spider.task_code.split('_')[0],
            # 抓取内容的时间
            'capture_at': getFormatTime(getNowTime()),
            'capture_timezone': getNowTime(),
        })
        capture_html_db.conn.insert(insert_item)
        return item


class SyncSystemDataPipeline(MongoPipeline):
    """
    同步数据类型爬虫数据管道
    任务配置的模式(mode)为2
    """

    def process_item(self, item, spider):
        spider.logger.info('Json数据管道启动,正在处理内容')
        proxy_db = MongoDB('pub_%s' % spider.task_resource or 'task_result')
        spider.logger.info('创建同步任务数据库连接 %s OK' % 'pub_%s' % spider.task_resource or 'task_result')
        try:

            # 根据task_resource分配储存的数据集,分派不同的储存流程
            if spider.task_resource == 'proxy_ip':
                self.process_sync_proxy(item['data'], proxy_db)
            elif spider.task_resource == 'category':
                self.process_sync_category(item['data'], proxy_db)
            elif spider.task_resource == 'product':
                self.process_sync_prodcut(item['data'], proxy_db)
            elif spider.task_resource == 'keyword':
                self.process_sync_keyword(item['data'], proxy_db)
            elif spider.task_resource == 'variant':
                self.process_sync_variant(item['data'], proxy_db)

        except Exception as e:
            spider.logger.error('数据库写入失败')
            spider.logger.error(e)
        return item

    def open_spider(self, spider):
        # spider (Spider 对象) – 被开启的spider
        # 可选实现，当spider被开启时，这个方法被调用。

        # 更新Spider接收到的任务信息
        print('Load in SyncSystemDataPipeline')
        sync_task_db = SyncTaskModel()
        spider.task = sync_task_db.conn.find_one(filter={'task_code': spider.task_code, 'rule_code': spider.rule_code})
        if spider.task is None:
            # 创建新的同步任务记录
            task_id = sync_task_db.conn.insert(dict({
                'updated_at': getFormatTime(getNowTime()),
                'cur_page': 1,
                'end_page': spider.request_end_page,
                'task_code': spider.task_code,
                'rule_code': spider.rule_code}))
            spider.task = sync_task_db.conn.find_one({'_id': task_id})
        pass

    def process_sync_proxy(self, data, db):
        """
        储存同步代理IP库
        :param data:
        :param db:
        """
        try:
            for response_item in data:
                response_item.update({'sync_at': getFormatTime(getNowTime())})
                db.conn.find_one_and_update({'proxy_ip': response_item['proxy_ip']},
                                            {'$set': dict({'weight': 0, 'use_count': 0}, **response_item)},
                                            projection={'proxy_ip': True, '_id': True},
                                            upsert=True,
                                            return_document=ReturnDocument.AFTER)
                logging.info(msg='爬虫同步代理IP [%s] OK!' % response_item['proxy_ip'])
        except Exception as e:
            logging.error('爬虫同步代理IP失败!', data=data)

    def process_sync_category(self, data, db):
        """
        储存同步产品分类
        :param data:
        :param db:
        """
        try:
            for response_item in data:
                response_item.update({'sync_at': getFormatTime(getNowTime())})
                res = db.conn.find_one_and_update({'id': response_item['id']},
                                                  {'$set': dict({}, **response_item)},
                                                  projection={'code': True, '_id': False},
                                                  upsert=True,
                                                  return_document=ReturnDocument.AFTER)
                logging.info(msg='爬虫同步Amazon产品分类 [%s] OK!' % response_item['title'])
        except Exception as e:
            logging.error('爬虫同步Amazon产品分类失败!', data=data)

    def process_sync_prodcut(self, data, db):
        """
        储存同步产品分类
        :param data:
        :param db:
        """
        try:
            for response_item in data:
                response_item.update({'sync_at': getFormatTime(getNowTime())})
                res = db.conn.find_one_and_update({'id': response_item['id']},
                                                  {'$set': dict({}, **response_item)},
                                                  projection={'sku': True, '_id': False},
                                                  upsert=True,
                                                  return_document=ReturnDocument.AFTER)
                logging.info(msg='爬虫同步产品数据SKU [%s] OK!' % response_item['sku'])
        except Exception as e:
            logging.error('爬虫同步产品SKU失败!', data=data)

    def process_sync_keyword(self, data, db):
        try:
            for response_item in data:
                response_item.update({'sync_at': getFormatTime(getNowTime())})
                res = db.conn.find_one_and_update({'id': response_item['id']},
                                                  {'$set': dict({}, **response_item)},
                                                  projection={'id': True, 'title': True, '_id': False},
                                                  upsert=True,
                                                  return_document=ReturnDocument.AFTER)
                logging.info(msg='爬虫同步关键词 [%s] OK!' % response_item['title'])
        except Exception as e:
            logging.error('爬虫同步关键词失败', data=data)
        pass

    def process_sync_variant(self, data, db):
        try:
            for response_item in data:
                response_item.update({'sync_at': getFormatTime(getNowTime())})
                res = db.conn.find_one_and_update({'id': response_item['id']},
                                                  {'$set': dict({}, **response_item)},
                                                  projection={'id': True, 'code': True, 'name': True, '_id': False},
                                                  upsert=True,
                                                  return_document=ReturnDocument.AFTER)
                logging.info(msg='爬虫同步变量表变量 [%s] OK!' % response_item['code'])
        except Exception as e:
            logging.error('爬虫同步变量失败', data=data)
        pass
