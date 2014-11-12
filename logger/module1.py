#!/usr/bin/env python
# encoding: utf-8


'''
dictConfig - 定义说明 https://docs.python.org/2/library/logging.config.html
Formatter - 自定义参数 https://docs.python.org/2/library/logging.html#logging.LogRecord
Handler - 内置类 https://docs.python.org/2/library/logging.handlers.html
'''


import logging
from logging import config


DEBUG = False


class RequireDebugFalse(logging.Filter):
    def filter(self, record):
        return not DEBUG


class RequireDebugTrue(logging.Filter):
    def filter(self, record):
        return DEBUG


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            # 这里定义的导入路径必须是 python path 下的导入路径
            '()': 'module1.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'module1.RequireDebugTrue'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'WARNING',
            'filters': ['require_debug_false'],
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'test.log',
            'when': 'S',
            'interval': 20,
            'backupCount': 5,
        },
    },
    'loggers': {
        # 如果新增 django.file logger 注意 propagate 问题
        # 可以通过设置propagate: False 阻止向父logger传递
        'django': {
            'level': 'ERROR',
            'handlers': ['file', 'console'],
        },
    }
}


config.dictConfig(LOGGING)
logger = logging.getLogger('django.file.%s' % __name__)


try:
    raise Exception('test Logger!')
except Exception, e:
    logger.exception(e)
