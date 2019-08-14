# -*- coding: utf-8 -*-

import sys,os
import time, socket
import peewee
from app.lib.db import pgDbClection

'''运程服务器日志'''
class Na_Product_Asin(peewee.Model):
    id = peewee.IntegerField()
    sku = peewee.CharField()
    asin = peewee.CharField()
    platform = peewee.CharField()
    sort = peewee.IntegerField()
    status = peewee.IntegerField(default=1),
    creator_id = peewee.IntegerField(default=1)
    platform_id = peewee.IntegerField(default=1)
    combine_type = peewee.IntegerField(default=1)
    updated_at = peewee.DateField()
    created_at = peewee.DateField(default=time.strftime("%Y-%m-%d %H:%M:%S"))

    class Meta:
        database = pgDbClection().Conn()