# coding:utf-8

import logging
import django.utils.log
import logging.handlers
from core.constants import BASE_DIR

# print(BASE_DIR)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # 禁用已经存在的logger实例
    'formatters': {
       'standard': {   #标准日志格式
            # 'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'  #日志格式
            'format': '[%(levelname)s][%(asctime)s][%(threadName)s:%(thread)d][%(filename)s:%(lineno)d]%(message)s'
        },
        'simple': {    # 简单的日志格式
            'format': '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
        },
        'collect': {   # 定义一个特殊的日志格式
            'format': '%(message)s'
        }
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },

    },
    'handlers': {
        'console':{
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'default': {
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR+'/var/logs/all.log',     #日志输出文件
            'maxBytes': 1024*1024*50,                  #文件大小
            'backupCount': 3,                         #备份份数
            'formatter':'standard',                   #使用哪种formatters日志格式
            'encoding': 'utf-8',
        },
        'error': {
            'level':'ERROR',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR+'/var/logs/error.log',
            'maxBytes':1024*1024*50,
            'backupCount': 3,
            'formatter':'standard',
            'encoding': 'utf-8',
        },
        'collect': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR+'/var/logs/collect.log',
            'maxBytes': 1024*1024*50,
            'backupCount': 3,
            'formatter':'collect',
            'encoding': 'utf-8',
        },
        'scprits_handler': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename':BASE_DIR+'/var/logs/script.log',
            'maxBytes': 1024*1024*50,
            'backupCount': 3,
            'formatter':'standard',
            'encoding': 'utf-8',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': False,
        }
    },
    'loggers': {
        'django': {
            'handlers': ['default', 'console', 'error'],
            'level': 'DEBUG',
            'propagate': True
        },
        # 'django.request': {
        #     'handlers': ['request_handler'],
        #     'level': 'ERROR',
        #     'propagate': False,
        # },
        'collect': {
            'handlers': ['console', 'collect'],
            'level': 'INFO',
        },
        'scripts': {
            'handlers': ['scprits_handler'],
            'level': 'INFO',
            'propagate': False
        },
        'sourceDns.webdns.views': {
            'handlers': ['default', 'error'],
            'level': 'ERROR',
            'propagate': True
        },
        # 'sourceDns.webdns.util':{
        #     'handlers': ['error'],
        #     'level': 'ERROR',
        #     'propagate': True
        # }
    }
}