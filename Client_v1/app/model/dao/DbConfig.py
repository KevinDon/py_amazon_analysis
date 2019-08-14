# coding:utf-8

from app.lib.db import *


class DbConfig(BaseDbModel):
    id = peewee.PrimaryKeyField()
    fid = peewee.IntegerField(null=False, default=0)
    name = peewee.TextField(null=False)
    main_key = peewee.TextField(null=False)
    minor_key = peewee.TextField(null=True)
    value = peewee.TextField(null=False)
    tip = peewee.TextField(null=True)
    type = peewee.IntegerField(null=False, default=2)
    sort = peewee.IntegerField(null=False, default=0)

    class Meta:
        order_by = ('sort',)
        db_table = 'na_config'