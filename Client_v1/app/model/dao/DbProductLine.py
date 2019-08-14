# @Time : 2019/7/16 13:56 
# @Author : Kevin
# @File : DbProductLine.py 
# @Software: PyCharm
# -*- coding: utf-8 -*-

import sys,os
import time, socket
import peewee
from app.lib.db import pgDbClection

'''运程服务器日志'''
class Na_Product_Line(peewee.Model):
    id = peewee.IntegerField()
    title = peewee.CharField()
    code = peewee.CharField()
    platform_id = peewee.IntegerField(default=1)
    platform = peewee.CharField()
    sort=peewee.IntegerField(default=0)
    status = peewee.IntegerField(default=1)
    parent_id=peewee.IntegerField()
    creator_id = peewee.IntegerField(default=1)
    updated_at = peewee.DateField(default=time.strftime("%Y-%m-%d %H:%M:%S"))
    created_at = peewee.DateField(default=time.strftime("%Y-%m-%d %H:%M:%S"))

    class Meta:
        database = pgDbClection().Conn()