# coding:utf-8

from app.lib.db import *

'''
本地插件表
'''
class DbPlusInFunction(BaseDbModel):
    id = peewee.PrimaryKeyField()
    fid = peewee.IntegerField(null=False, default=0)
    title_cn = peewee.TextField(null=False)
    title_en = peewee.TextField(null=False)
    field_type = peewee.IntegerField(null=False, default=2)
    field = peewee.TextField(null=True, default=2)
    url = peewee.TextField(null=True)
    is_path = peewee.IntegerField(null=True, default=2)
    method = peewee.TextField(null=False, default='get')
    sort = peewee.IntegerField(null=False, default=0)
    context = peewee.TextField(null=True)

    class Meta:
        order_by = ('sort',)
        db_table = 'na_plusin_functions'