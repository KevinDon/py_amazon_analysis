# @Time : 2019/7/16 17:30 
# @Author : Kevin
# @File : DbAmazonProductCategory.py 
# @Software: PyCharm

# -*- coding: utf-8 -*-

import sys,os
import time, socket
import peewee
from app.lib.db import pgDbClection

'''运程服务器日志'''
class Amazon_Product_Category(peewee.Model):
    id = peewee.IntegerField()
    title = peewee.CharField()
    code = peewee.CharField()
    platform_id = peewee.IntegerField(default=1)
    platform = peewee.CharField()
    sort=peewee.IntegerField(default=0)
    status = peewee.IntegerField(default=1)
    level=peewee.IntegerField(default=0)
    parent_id=peewee.IntegerField()
    creator_id = peewee.IntegerField(default=1)
    updated_at = peewee.DateField(default=time.strftime("%Y-%m-%d %H:%M:%S"))
    created_at = peewee.DateField(default=time.strftime("%Y-%m-%d %H:%M:%S"))

    class Meta:
        database = pgDbClection().Conn()

    def add(self, **entries):
        try:
            pubScriptResult = Amazon_Product_Category()
            pubScriptResult.__dict__.update(entries)
            pubScriptResult.save()
        except Exception as e:
            print(e)

    '''根据Title查询记录'''
    def getIdByTitle(self, title):
        try:
            row = Amazon_Product_Category().select().where(Amazon_Product_Category.title == title).get()
            return row.id
        except Amazon_Product_Category.DoesNotExist:
            return 0
        pass

    '''根据code查询记录'''
    def getRowByCode(self, code):
        try:
            row = Amazon_Product_Category().select().where(Amazon_Product_Category.code == code).get()
            return row
        except Amazon_Product_Category.DoesNotExist:
            return 0
        pass