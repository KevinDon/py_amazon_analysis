# coding:utf-8
from django.db import connections


class ResultData():
    # 数据表名
    _table_name = None

    # 表字段
    _fields = []

    # 字段值
    _values = []

    # 提炼到的SQL集
    _sqls = []

    def __init__(self, tableName, fields=[]):
        self._table_name = tableName
        self._fields = fields
        self._values = []
        self._sqls = []
        pass

    '''创建数据插入语句'''
    def createInsert(self, **maps):
        fields = ['"%s"' % str(i) for i in self._fields]
        base_sql = "INSERT INTO " + self._table_name + " (" + ','.join(fields) + ") VALUES "
        _values = []
        for value_list in maps['values']:
            value_list = ["'%s'" % self.transferContent(str(i)) for i in value_list]
            self._values.append(value_list)
            _values.append("(%s)" % ','.join(value_list))
        sql = '%s%s' % (base_sql, ', '.join(_values))
        self._sqls.append(sql)
        return sql

    '''执行数据插入'''
    def executeInsert(self):
        result = []
        try:
            with connections['default'].cursor() as cursor:
                for sql in self._sqls:
                    result.append(cursor.execute(sql))
                self._sqls = []
            return result
        except Exception as e:
            import traceback
            traceback.print_exc()
            return result

    '''特殊字符处理'''
    def transferContent(self, content):
        if content is None:
            return ''
        else:
            string = content.replace("'", "''")
            string = string.replace("%", "%%")
            return string