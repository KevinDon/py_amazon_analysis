# -*- coding: utf-8 -*-
import datetime

# 格林威治时间
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'


def getNowTime():
    """
    获取当前时间戳
    :return:
    """
    # return datetime.datetime.now().timestamp().
    # utc
    return datetime.datetime.utcnow().timestamp()


def getFormatTime(time_stamp, format_str=TIME_FORMAT):
    """
    格式化时间
    :param time_stamp: 戳
    :param format_str: 格式
    :return:
    """
    if type(time_stamp) is float:
        time_stamp = datetime.datetime.fromtimestamp(time_stamp)
    return time_stamp.strftime(format_str)


def getDifferTime(end, begin):
    """
    计算时间差
    :param end: 戳 或 strtime
    :param begin: 戳 或 strtime
    :return:
    """
    if type(end) is float:
        end = datetime.datetime.fromtimestamp(end)
    if type(begin) is float:
        begin = datetime.datetime.fromtimestamp(begin)

    return (end - begin).seconds


def mongo_collection_get(table=None, filter_dict=None):
    if table is None:
        raise Exception('Mongo DB query collection name can not be None')

    def decorator(func):
        def wrapper(*args, **kwargs):
            from core.libs.MongoDbHandler import MongoDB
            variant_db = MongoDB(table)
            variant_row = list(variant_db.conn.find(filter_dict))
            if len(variant_row) < 1:
                raise Exception('Spider match nothing')
            elif len(variant_row) > 1:
                raise Exception('Spider match too much result')
            # variant_row_list = variant_row[0].get('value').split('\r\n')
            return func(result=variant_row[0])

        return wrapper

    return decorator


@mongo_collection_get(table='pub_variant', filter_dict={'code': 'capture_rule_resource_list'})
def getVariantValueList(*args, **kwargs):
    result = kwargs.get('result')
    values_list = result.get('value').split('\r\n')
    return values_list
    pass


class singleInstanceClass(object):
    import threading
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(singleInstanceClass, "_instance"):
            with singleInstanceClass._instance_lock:
                if not hasattr(singleInstanceClass, "_instance"):
                    singleInstanceClass._instance = object.__new__(cls)
        return singleInstanceClass._instance


class numCounter(object):
    initial_val = 0
    counter = 0  # type: int
    name = None

    def __def__(self, name, initial_val=0):
        self.name = name
        self.initial_val = initial_val
        self.counter = initial_val

    def inc(self, num=1):
        """

        :type num: int
        """
        self.add(num)

    def add(self, num=0):
        """

        :type num: int
        """
        self.counter += num

    def sub(self, num=0):
        """

        :type num: int
        """
        self.counter -= num

    def __repr__(self, *args, **kwargs):
        return str(self.counter)

    def rz(self):
        self.counter = self.initial_val
