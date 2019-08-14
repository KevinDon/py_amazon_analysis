# @Time : 2019/7/18 17:48 
# @Author : Kevin
# @File : DbSkuKeyword.py
# @Software: PyCharm
# coding:utf-8

import sys,os
import time, socket
import peewee
from app.lib.db import pgDbClection
from app.lib.logger import Log
'''运程服务器日志'''
class Pub_Sku_Keyword(peewee.Model):
    id = peewee.IntegerField()
    title = peewee.CharField()
    platform = peewee.CharField()
    platform_id = peewee.IntegerField(default=0)
    status = peewee.CharField()
    sort = peewee.CharField()
    keyword_type = peewee.IntegerField(default=1)
    creator_id = peewee.IntegerField()
    updated_at = peewee.DateField(default=time.strftime("%Y-%m-%d %H:%M:%S"))
    created_at = peewee.DateField(default=time.strftime("%Y-%m-%d %H:%M:%S"))

    class Meta:
        database = pgDbClection().Conn()

    def keywordListAll(self):
        """
        获取全部记录
        :return: result list
        """
        try:
            rows = Pub_Sku_Keyword.select().order_by(Pub_Sku_Keyword.updated_at.desc()).dicts()
        except Exception as e:
            Log().error('查询数据失败')
            Log().error(e)

        return rows
