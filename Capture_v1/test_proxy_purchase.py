import urllib.request
import random
import requsets
if __name__ == '__main__':
    username = 'lum-customer-hl_b84c314f-zone-static'
    password = '5eu4ypkeqsj5'
    port = 22225
    session_id = random.random()
    super_proxy_url = ('http://%s-country-au-session-%s:%s@zproxy.lum-superproxy.io:%d' %
                       (username, session_id, password, port))
    proxy_handler = urllib.request.ProxyHandler({
        'http': super_proxy_url,
        'https': super_proxy_url,
    })
    opener = urllib.request.build_opener(proxy_handler)
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0')]
    print('Performing request')
    print(opener.open('http://lumtest.com/myip.json').read())


    def get_proxy_by_channel():
        username = 'lum-customer-hl_b84c314f-zone-static'
        password = '5eu4ypkeqsj5'
        port = 22225
        session_id = random.random()
        return ('http://%s-country-au-session-%s:%s@zproxy.lum-superproxy.io:%d' %
                (username, session_id, password, port))


    print(requsets.api.post(get_proxy_by_channel()))
