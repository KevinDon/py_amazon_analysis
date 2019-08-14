# -*- coding:utf8 -*-
import os, sys
import peewee
from app.lib.logger import Log as logger

class BaseDbModel(peewee.Model):
    class Meta:
        curPath, filename = os.path.split(os.path.abspath(sys.argv[0]))
        database = peewee.SqliteDatabase(curPath +'/app/resource/data.db')


'''本地配置'''
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

'''
服务器数据库定义
'''
class pgDbClection:
    def Conn(self):
        # confs = DbConfig.select()
        leDbHost = DbConfig().get(main_key='setting', minor_key='leDbHost')
        leDbPort = DbConfig().get(main_key='setting', minor_key='leDbPort')
        leDbName = DbConfig().get(main_key='setting', minor_key='leDbName')
        leDbUsername = DbConfig().get(main_key='setting', minor_key='leDbUsername')
        leDbPassword = DbConfig().get(main_key='setting', minor_key='leDbPassword')

        try:
            conn = peewee.PostgresqlDatabase(
                leDbName.value
                , host=leDbHost.value
                , port=int(leDbPort.value)
                , user=leDbUsername.value
                , password=leDbPassword.value
                , encoding='utf8'
            )
            return conn
        except Exception as e:
            print(e)

        pass

'''创建数据库链接'''
try:
    pbConn = pgDbClection().Conn()
except Exception as e:
    logger.info(e)

'''PgSQL数据库基础类'''
class BasePgDbModel(peewee.Model):

    class Meta:
        database = pbConn