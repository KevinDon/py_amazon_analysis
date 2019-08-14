# coding:utf-8
import datetime


def QueryBuildToStr(ent, conditions):
    # print(conditions)
    _where = ''
    if len(conditions) > 0:
        _union = ''
        for item in conditions:
            if (_union == ''):
                _where = '({0}.{1} {2} {3})'.format(ent, item[0], _getOptions(item[1],item[4]), _getValue(item[1],item[2],item[4]))
                _union = item[3]
            else:
                if _union == 'AND':
                    _where += ' & ({0}.{1} {2} {3})'.format(ent, item[0], _getOptions(item[1],item[4]), _getValue(item[1],item[2],item[4]))
                else:
                    _where += ' | ({0}.{1} {2} {3})'.format(ent, item[0], _getOptions(item[1],item[4]), _getValue(item[1],item[2],item[4]))
                _union = item[3]

    # print(_where)
    return _where

def _getOptions(opteion, type='string'):
    if opteion == '=' :
        return '=='
    elif opteion == 'contains' :
        if type == 'date':
            return '=='
        else:
            return '**'
    else:
        return opteion

def _getValue(opteion, value, type='string'):
    if opteion == 'contains' :
        if type == 'date':
            return 'datetime.datetime.strptime("{0}", "{1}")'.format(value, '%Y-%m-%d %H:%M:%S')
        else:
            return '"%{0}%"'.format(value)
    else:
        if type == 'date':
            return 'datetime.datetime.strptime("{0}", "{1}")'.format(value, '%Y-%m-%d %H:%M:%S')
        else:
            return '"{0}"'.format(value)