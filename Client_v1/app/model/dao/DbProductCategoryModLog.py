# @Time : 2019/7/13 11:11 
# @Author : Kevin
# @File : DbProductCategoryModLog.py.py
# @Software: PyCharm
# -*- coding: utf-8 -*-

# @Time : 2019/7/2 19:40
# @Author : Kevin
# @File : DbProductCategory.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
import sys,os
import time, socket
import peewee
from app.lib.db import pgDbClection

'''运程服务器日志'''
class Pub_Product_Category_Mod_Log(peewee.Model):
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

