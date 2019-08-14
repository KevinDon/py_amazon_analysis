# coding:utf-8
from lxml import etree


class XmlObject:

    _obj = None
    # 根节点
    _treeroot = None

    # TODO 构造方法，可以加预置格式校验
    def __init__(self, xmlstr=None, type="xml"):
        # xmlstr = xmlstr.encode('utf-8')
        if type == 'html':
            self._obj = etree.HTML(xmlstr)
        else:
            self._obj = etree.XML(xmlstr.encode('utf-8'))
        self._treeroot = None

    # TODO 根据元素名、元素名、xpath及元素index获取匹配的元素内容
    '''可根据元素名、xpath + group 获取元素'''
    def getElement(self, name='', xpath='', group=None):
        _result = None
        if name is not '':
            _result = self._obj.find(name)
        else:
            _list = self._obj.xpath(xpath)
            _result = _list if group is None else _list[group]
        return _result


    # 获取全部内容
    def getXmlContent(self):

        pass


    # TODO 获取所有属性
    '''获取节点所有属性，返回(tuple)'''
    def getAttrs(self):

        pass


    # TODO 可用正则表达式获取属性的值
    '''可用正则表达式获取某个属性的值'''
    def getAttr(self, name, pattern='', group=-1):

        pass


    '''判断某属性是否存在'''
    def hasAttr(self, name):

        pass


    # TODO 可用正则表达式提取节点内容
    def getContent(self, pattern='', group=-1):

        pass



    '''判断某元素是否存在'''
    def hasElement(self, name='', xpath= '', group=0):

        pass

