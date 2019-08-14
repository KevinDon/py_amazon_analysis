# -*- coding: utf-8 -*-
import logging
import os
import configparser

from core.libs.CommonUnit import singleInstanceClass


class LocalConfigHandler(singleInstanceClass):
    import threading
    _instance_lock = threading.Lock()
    config = None  # type configparser.ConfigParser()

    def __init__(self, cfg_path=None, cfg_name=None):
        """
        根据task_name读取本地同步任务和资源配置
        :param cfg_path: 配置文件路径
        :param cfg_name: 配置文件名
        """
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        cfg_path = os.path.abspath(os.path.join(BASE_DIR, '..', cfg_name or 'config.cfg'))  # scrapyd
        logging.info('爬虫加载本地配置文件 %s' % cfg_path)
        conf_file = configparser.ConfigParser()
        if conf_file.read(cfg_path, encoding='utf-8-sig'):
            self.config = conf_file
        else:
            raise Exception('Spider loading local config file failed!')


if __name__ == '__main__':
    local = LocalConfigHandler()
    pass
