# @Time : 2019/7/16 17:42 
# @Author : Kevin
# @File : DbAmazonPorductCategpryModLog.py 
# @Software: PyCharm
# -*- coding: utf-8 -*-
import sys,os
import time, socket
import peewee
from app.lib.db import pgDbClection

'''运程服务器日志'''
class Amazon_Product_Category_Mod_Log(peewee.Model):
    id = peewee.IntegerField()
    category = peewee.CharField()
    modify_fields = peewee.CharField()
    old_val = peewee.TextField(null=False, )
    new_val = peewee.TextField(null=False, )
    status = peewee.IntegerField()
    sort = peewee.IntegerField()
    creator_id = peewee.CharField()
    updated_at = peewee.DateField(default=time.strftime("%Y-%m-%d %H:%M:%S"))
    created_at = peewee.DateField(default=time.strftime("%Y-%m-%d %H:%M:%S"))

    class Meta:
        database = pgDbClection().Conn()

