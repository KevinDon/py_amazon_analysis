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
class Pub_Product_Category(peewee.Model):
    id = peewee.IntegerField()
    title = peewee.CharField()
    code = peewee.CharField()
    sort=peewee.IntegerField(default=0)
    status = peewee.IntegerField(default=1)
    # leaf = peewee.IntegerField(default=1)
    level=peewee.IntegerField(default=0)
    parent_id=peewee.IntegerField()
    creator_id = peewee.IntegerField(default=1)
    updated_at = peewee.DateField(default=time.strftime("%Y-%m-%d %H:%M:%S"))
    created_at = peewee.DateField(default=time.strftime("%Y-%m-%d %H:%M:%S"))

    class Meta:
        database = pgDbClection().Conn()

    def add(self, **entries):
        try:
            pubScriptResult = Pub_Product_Category()
            pubScriptResult.__dict__.update(entries)
            pubScriptResult.save()
        except Exception as e:
            print(e)

    '''根据Title查询记录'''
    def getIdByTitle(self, title):
        try:
            row = Pub_Product_Category().select().where(Pub_Product_Category.title == title).get()
            return row.id
        except Pub_Product_Category.DoesNotExist:
            return 0
        pass

    '''根据code查询记录'''
    def getRowByCode(self, code):
        try:
            row = Pub_Product_Category().select().where(Pub_Product_Category.code == code).get()
            return row
        except Pub_Product_Category.DoesNotExist:
            return 0
        pass