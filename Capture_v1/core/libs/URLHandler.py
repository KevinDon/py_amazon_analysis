import re



class URLHandler:
    protocol_pool = ('http', 'https', 'mailto')

    protocol = None  # 网络协议 http or https
    url = None  # url
    host = None  # 主机地址
    port = None  # 端口
    version = None  # 端口版本号
    url_path = None  # 接口地址

    username = None
    password = None

    path = None
    path_variants = {}
    params = None
    params_variants = {}

    def __init__(self, **kwargs):
        """
        :param url_mode:
        :param url_protocol:
        :param kwargs:
        """

        for item, value in kwargs.items():
            if kwargs.get('url'):
                self.load_url(kwargs.get('url'))
            self.__setattr__(item, value)
            # 传递的参数中拥有url,则会先根据url进行解析

    def get_api(self):
        if self.port:
            host = '%s:%s' % (self.host, self.port)
        else:
            host = self.host

        return '%s://%s/' % (
            self.protocol,
            '/'.join((
                host,
                self.version,
                self.url_path
            ))
        )

    def load_url(self, url: str = None):
        if url:
            # 分析url
            str_parts = url.split('://')

            if len(str_parts) > 1 and self.has_protocol(url):
                # url中包含协议头
                self.protocol = str_parts[0]
                url_parts = str_parts[1].split('/')
                self.host = url_parts[0]

            elif len(str_parts) > 2:
                raise Exception('Error , Url is not correct Url')

    @classmethod
    def has_protocol(cls, url: str = None, match_protocol: tuple = None, has_return=False):

        match_protocol = match_protocol or cls.protocol_pool
        match_url = url or ''
        match_bool = False
        match_flag = None

        for protocol in match_protocol:
            match_flag = re.match('^(%s)://' % protocol, match_url)
            match_bool = match_flag is not None
            if match_bool:
                break

        if has_return:
            return match_bool, match_flag
        else:
            return match_bool


if __name__ == '__main__':
    test_url = 'https://www.baidu.com/abc/bcd/?h=f&i=123'
    u = URLHandler()
    res = u.has_protocol(test_url)
