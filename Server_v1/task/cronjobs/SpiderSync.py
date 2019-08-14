# coding:utf-8

import requests, datetime, time
from django.core.handlers.base import logger


def SpiderSync(serverId, spiderName=None):
    from system.model import ServerConfigModel

    _result = False
    beginTime = datetime.datetime.now()
    if spiderName is None:
        logger.error('error: {0} |{1}'.format((datetime.datetime.now() - beginTime).seconds, '爬虫同步任务启动,需要指定爬虫名'))
        return False
    try:
        logger.info('Send Command of CaptureSpider: {0}'.format(beginTime.strftime('%H:%M:%S')))

        _spiderServer = ServerConfigModel.objects.get(id=serverId)

        # 拼装命令
        _url = 'http://{0}:{1}/schedule.json'.format(_spiderServer.ip, _spiderServer.port)
        _data = {"project": 'default',
                 "spider": spiderName,
                 "task_code": '%s_%s' %(spiderName, _spiderServer.ip),
                 "rule_code": '%s_%s' %(spiderName, _spiderServer.ip),
                 # "rule": StringZipper.b64encode(StringZipper.zip(XML_obj.get_xml()))
                 "rule": ''
                 }

        requests.post(url=_url, data=_data)

        # 'curl http://localhost:5500/schedule.json -d project=default -d spider=TestSpider -d code=xxx'
        _result = True
    except Exception as e:
        logger.error('error: {0} | {1}'.format((datetime.datetime.now() - beginTime).seconds, e))

    logger.info('End for send command of CaptureSpider: {0} s'.format((datetime.datetime.now() - beginTime).seconds))

    return _result
