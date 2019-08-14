# coding:utf-8

import re
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from app.lib.logger import Log
import time
import peewee

'''全局Log对象'''
logger = Log('info')

'''将None转换为目标类型'''
def utNone2Object(o, default=''):
    return o if (o is not None) else default

'''创建 QTableWidgetItem 项'''
def utQTableWidgetItem(value, default=''):
    return QTableWidgetItem('{0}'.format(utNone2Object(value, default)))

def utStr2Date(value, default=''):
    return re.search('\d{4}-\d{1,2}-\d{1,2}', value).group(0) if (re.search('\d{4}-\d{1,2}-\d{1,2}', value) is not None) else ''

'''字符串中提取第一个浮点小数'''
def utStr2Float(value, default= 0.00):
    result = default
    if (re.search('\d{0,}\.\d{0,}', value) is not None):
        result = float(re.search('\d{0,}\.\d{0,}', value).group(0))
    elif(re.search('\d{0,}', value) is not None):
        result = float(re.search('\d{0,}', value).group(0))
    return result

'''字符串中提取第一个整数'''
def utStr2Int(value, default= 0):
    return int(re.search('\d{0,}', value).group(0)) if (re.search('\d{0,}', value) is not None) else default

def utGetStyleContent(rootPath, styleName):
    style = ''
    try:
        with open('%s/app/resource/css/%s.css' %(rootPath, styleName), encoding='utf-8') as file:
            style = file.readlines()
            style = "".join(style).strip('\n')
    except Exception as e:
        logger.info(e)
    return style


'''时间'''
def getTime(time_stamp=False, time_format='%Y.%m.%d %H:%M:%S'):
    """
    获取时间
    :return:
    :param time_stamp: time.time()
    :param time_format: '%Y.%m.%d %H:%M:%S'
    :return:
    """
    return time.strftime(time_format, time.localtime(time_stamp if time_stamp else time.time()))


def getModelFields(model, keepers=[], filters=[]):
    """
    获取数据模型的字段
    :param model: 数据模型
    :param keepers: 保留字段
    :param filters: 过滤字段
    :return: 字段集合
    """
    res = {}
    fields = model.__dict__
    for field in fields:
        if type(fields[field]) is peewee.FieldAccessor and (field not in filters or field in keepers):
            res[field] = fields[field]
    return res

def qt5TableRowAppendField(table, row_id=None, col_id=None, default_val=str(2)):
    """
    qt5表格追加编辑列
    :param table: QTableWidget
    :param row_id:  行id
    :param col_id: 列id
    :param default_val: 默认值
    """
    try:
        if row_id is None:
            raise Exception('缺少Row_id')
        if col_id is None:
            raise Exception('缺少Col_id')
        newItem = QTableWidgetItem(str(default_val))
        table.setItem(row_id, col_id, newItem)
    except Exception as e:
        # import traceback;
        # traceback.print_exc();
        logger.error('qt5Table追加编辑列,%s' % e)


def qt5TableLoadDatas(table, new_datas, fields, has_edit_flag=False, process_bar=False, is_return=False,  is_auto_fixed=False, is_can_sort=False, checkModel=False):
    """
    qt5 table widget加载数据
    :param table:
    :param new_datas:
    :param fields:
    :param has_edit_flag: 追加编辑标记列
    :param process_bar:
    :param is_return:
    :param is_auto_fixed: 是否自动缩放表头
    """
    try:
        cache_return = []
        fields_count = len(fields) + 1 if has_edit_flag else len(fields)
        table.setSortingEnabled(False)
        table.setColumnCount(fields_count)
        table.setHorizontalHeaderLabels(
            dict(fields, **{'is_edit': '已编辑'}).values() if has_edit_flag else fields.values())
        # table.setColumnHidden(0, show_id is False)
        table.horizontalHeader().setSectionResizeMode(1 if is_auto_fixed else 0)
        table.setRowCount((len(new_datas) or 14))
        i = 0
        if len(new_datas) > 0:
            for row in new_datas:
                fields_list = list(fields)
                for k in list(fields):
                    newItem = QTableWidgetItem(str(row[k]))


                    table.setItem(i, fields_list.index(k), newItem)

                # 追加编辑字段
                if has_edit_flag:
                    qt5TableRowAppendField(table, i, fields_count - 1)
                if process_bar:
                    process_bar.setValue(process_bar.value() + 1)
                i = i + 1
                cache_return.append(row) if is_return else None
        else:
            raise Exception('表格字段设置出错')
        table.setSortingEnabled(True) if is_can_sort else None

        return cache_return
    except Exception as e:
        logger.error('qt5Table加载数据出错,%s' % e)
    pass


def qt5TableRowAppendField(table, row_id=None, col_id=None, default_val=str(2)):
    """
    qt5表格追加编辑列
    :param table: QTableWidget
    :param row_id:  行id
    :param col_id: 列id
    :param default_val: 默认值
    """
    try:
        if row_id is None:
            raise Exception('缺少Row_id')
        if col_id is None:
            raise Exception('缺少Col_id')
        newItem = QTableWidgetItem(str(default_val))
        table.setItem(row_id, col_id, newItem)
    except Exception as e:
        # import traceback;
        # traceback.print_exc();
        logger.error('qt5Table追加编辑列,%s' % e)
    pass

def qt5TableSetHiddenHeaders(table, hidden_fields=None, table_fields=None, has_edit_flag=False):
    """
    设置Qt5Table 隐藏列
    :param table:
    :param hidden_fields: list
    :param table_fields:
    """
    try:
        if has_edit_flag:
            table_fields_all = dict(table_fields, **{'is_edit': '已编辑'})
        for i in hidden_fields:
            if type(i) is int:
                table.setColumnHidden(i, True)
            elif type(i) is str:
                hidden_index = [x for x, item in enumerate(table_fields_all) if item == i]
                table.setColumnHidden(hidden_index[0], True) if len(hidden_index) > 0 else None
            else:
                raise Exception('hidden_fields传入参数的类型不正确')

    except Exception as e:
        logger.error('qt5Table设置隐藏列出错,%s' % e)
