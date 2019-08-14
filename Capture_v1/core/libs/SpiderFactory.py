from core.libs.parts.SpiderCore import SpiderCore
from core.libs.parts.public.SpiderRuleParts import SpiderRuleParts
from core.libs.parts.public.SpiderTaskParts import SpiderTaskParts


class SpiderFactory(object):
    '''
    暂未使用
    '''
    @staticmethod
    def build_spider(name, core: tuple = (), parts: dict = {}, parts_default={}):
        """
        合成爬虫功能
        :param name:
        :param core:
        :param parts:
        :param parts_default:
        :return:
        """
        return type(name, core, parts)


if __name__ == '__main__':
    test_spider = SpiderFactory.build_spider('test_spider', (SpiderCore,),
                                             {'spider_parts': {
                                                 'rule': SpiderRuleParts,
                                                 'task': SpiderTaskParts}
                                             })
    pass
