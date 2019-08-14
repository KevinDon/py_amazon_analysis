# -*- coding: utf-8 -*-
from core.libs.CommonUnit import getFormatTime, getNowTime
from core.libs.MongoDbHandler import MongoDB, tableField


class ProxyIpPoolModel(MongoDB):
    class Meta:
        db_table = 'pub_proxy_ip'

    fields = dict(
        status=tableField(default=1),
        proxy_ip=tableField(),
        proxy_port=tableField(),
        agent_type=tableField(default=1),
        country=tableField(),
        regoin=tableField(),
        city=tableField(),
        created_at=tableField(),
        priority=tableField(default=100),
        sync_at=tableField(default=getFormatTime(getNowTime())),
    )

    pass


class ProxyChannelModel(MongoDB):
    class Meta:
        db_table = 'pub_proxy_channel'

    fields = dict(
        status=tableField(default=1),

    )

    pass


# if __name__ == '__main__':
#     import urllib.request
#     import random
#
#     username = 'lum-customer-hl_7cd782cc-zone-static'
#     password = 'rffbz47cy5ew'
#     port = 22225
#     session_id = random.random()
#     super_proxy_url = ('http://%s-country-au-session-%s:%s@zproxy.lum-superproxy.io:%d' %
#                        (username, session_id, password, port))
#     proxy_handler = urllib.request.ProxyHandler({
#         'http': super_proxy_url,
#         'https': super_proxy_url,
#     })
#     opener = urllib.request.build_opener(proxy_handler)
#     opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0')]
#     print('Performing request')
#     print(opener.open('http://lumtest.com/myip.json').read())
