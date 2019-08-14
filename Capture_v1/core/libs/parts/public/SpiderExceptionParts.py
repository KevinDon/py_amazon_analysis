import logging

import scrapy


class SpiderExceptionsParts(object):

    @staticmethod
    def log_exp(msg, module=None, method=None):
        logging.error(' - '.join((module, method, msg)))
