import datetime
import os
import django
import requests
from django.core.handlers.base import logger
import json


def handle():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")  # 你的django的settings文件
    django.setup()
    from system.model import ProxyIpModel
    result = False
    beginTime = datetime.datetime.now()
    message_type = "ProxyIpCheck"
    try:
        logger.info('Begin for {0}: {1}'.format(message_type, beginTime.strftime('%H:%M:%S')))
        ip_list = ProxyIpModel.objects.exclude(status=3).all()

        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',}
        for ip in ip_list:
            try:
                proxy = {'http':  'http://' + ip.proxy_ip+':'+ip.proxy_port,
                         'https':  'https://' + ip.proxy_ip+':'+ip.proxy_port}
                # print proxy
                res = requests.get("http://ip-api.com/json/"+ip.proxy_ip, proxies=proxy, timeout=10, headers=header)
                if res.status_code == 200:
                    ip.country = res.json()['country']
                    ip.region = res.json()['regionName']
                    ip.city = res.json()['city']
                    ip.test_result = 1
                    ip.save()
                else:
                    ip.test_result = 2
                    ip.save()
            except Exception as e:
                ip.test_result = 2
                ip.save()
                pass
    except Exception as e:
        logger.error('error: {0} | {1}'.format((datetime.datetime.now() - beginTime).seconds, e))
    logger.info('End for {0}: {1} s'.format(message_type, (datetime.datetime.now() - beginTime).seconds))
    return result


if __name__ == '__main__':
    handle()
