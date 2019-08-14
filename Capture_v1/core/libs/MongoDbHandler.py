import abc
import datetime
import logging
import random
import time

from pymongo import MongoClient
from core.libs.LocalConfigHandler import LocalConfigHandler

LOCAL_CONFIG = LocalConfigHandler()
MONGO_HOST = LOCAL_CONFIG.config.get('mongodb', 'mongodb_host')
MONGO_PORT = int(LOCAL_CONFIG.config.get('mongodb', 'mongodb_port'))
MONGO_DB_NAME = LOCAL_CONFIG.config.get('mongodb', 'mongodb_db_name')
MONGO_ITEM = LOCAL_CONFIG.config.get('mongodb', 'mongodb_db_item')
MONGO_USER = LOCAL_CONFIG.config.get('mongodb', 'mongodb_user')
MONGO_PASSWORD = LOCAL_CONFIG.config.get('mongodb', 'mongodb_password')


class MongoDB:
    """
    Mongo DB 连接类
    """
    conn = None
    fields = dict()

    def Conn(self):
        """
        根据类的meta.db_table设置,创建指定数据集的链接
        :return:
        """

        if self.conn:
            return self.conn
            pass
        else:
            host = MONGO_HOST
            port = MONGO_PORT
            db_name = MONGO_DB_NAME
            logging.info('爬虫连接MongoDB %s:%s-%s' % (host, port, db_name))
            client = MongoClient(host=host, port=port)
            # client = MongoClient(host=host, port=port, waitQueueTimeoutMS=2000)
            db = client[db_name]
            if MONGO_USER and MONGO_PASSWORD:
                db.authenticate(MONGO_USER, MONGO_PASSWORD)
            self.conn = db[self.Meta.db_table or MONGO_ITEM]
        return self.conn

    class Meta:
        db_table = None

    def __init__(self, db_table=None):
        if db_table:
            self.Meta.db_table = db_table
        try:
            self.conn = self.Conn()
        except Exception as e:
            logging.error('MongoDb连接失败', e)

    def get_fields(self):
        return self.fields

    def get_new_row(self, fields: tuple = ()):
        fields = fields or self.get_fields()
        return {item: self.fields.get(item).default() if callable(self.fields.get(item).default) else self.fields.get(item).default for item in fields}


class tableField(object):
    _field = 'tableField'
    _field_type = 'tableField'

    verbose_name = ''
    default = None

    def __init__(self, **kwargs):
        for item in kwargs:
            self.__setattr__(item, kwargs.get(item))
        pass

    def get_default(self):
        return self.default or ''


class UrlPoolModel(MongoDB):
    class Meta:
        db_table = None

    def __init__(self):
        super(UrlPoolModel, self).__init__(self.Meta.db_table)
