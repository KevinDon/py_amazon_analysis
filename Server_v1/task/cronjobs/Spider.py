# coding:utf-8
import requests, datetime, time
from django.core.handlers.base import logger


def CaptureSpider(ruleId):
    from task.model import TaskCaptureListModel
    from system.model import ServerConfigModel
    from rule.model import CaptureRuleModel
    from core.libs.string_zipper import StringZipper
    from rule.vo import CaptureRuleVo
    from rule.libs.XMLETConstructor import XMLETConstructor

    _result = False
    beginTime = datetime.datetime.now()

    try:
        logger.info('Send Command of CaptureSpider: {0}'.format(beginTime.strftime('%H:%M:%S')))

        # _job = TaskCaptureListModel.objects.get(rule_id=ruleId)
        _rule = CaptureRuleModel.objects.get(id=ruleId)
        _spiderServer = ServerConfigModel.objects.get(id=_rule.scrapy_server_id)

        _rule_dict = CaptureRuleVo(instance=_rule).data
        print(_rule_dict)
        XML_obj = XMLETConstructor(dict(_rule_dict))
        print(_rule_dict.get('spider_name'))
        # 拼装命令
        _url = 'http://{0}:{1}/schedule.json'.format(_spiderServer.ip, _spiderServer.port)
        _data = {"project": 'default',
                 # "spider": "CaptureSpider",
                 "spider": _rule_dict.get('spider_name',"CaptureSpider"),
                 # "spider": 'TestSpider',
                 "task_code": '%s_%s' % (_spiderServer.ip, _rule_dict.get('id')),
                 "rule_code": _rule.rule_code,
                 # "rule": StringZipper.b64encode(StringZipper.zip(XML_obj.get_xml()))
                 "rule": StringZipper.b64encode(StringZipper.zip(_rule_dict.get('xml_data').encode()))
                 }

        requests.post(url=_url, data=_data)

        # 'curl http://localhost:5500/schedule.json -d project=default -d spider=TestSpider -d code=xxx'
        _result = True
    except Exception as e:
        logger.error('error: {0} | {1}'.format((datetime.datetime.now() - beginTime).seconds, e))

    logger.info('End for send command of CaptureSpider: {0} s'.format((datetime.datetime.now() - beginTime).seconds))

    return _result
