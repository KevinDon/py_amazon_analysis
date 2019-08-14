# coding:utf-8

from app.lib.db import *

'''
本地插件表
'''
class DbPlusIn(BaseDbModel):
    id = peewee.PrimaryKeyField()
    fid = peewee.IntegerField(null=False, default=0)
    type = peewee.IntegerField(null=False, default=2)
    code = peewee.TextField(null=False)
    title_cn = peewee.TextField(null=False)
    title_en = peewee.TextField(null=False)
    url = peewee.TextField(null=True)
    account = peewee.TextField(null=True)
    password = peewee.TextField(null=True)
    method = peewee.TextField(null=True)
    protocol = peewee.TextField(null=True)
    shortcut = peewee.TextField(null=True)
    javascript = peewee.TextField(null=True)  # 可用于自动登录
    is_system = peewee.IntegerField(default=2)
    is_display = peewee.IntegerField(default=2)
    created_at = peewee.DateTimeField(null=True)
    sort = peewee.IntegerField(default=0)

    class Meta:
        order_by = ('sort',)
        db_table = 'na_plusin'
