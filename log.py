#!/usr/bin/env python
# encoding: utf-8


import os
import logging
import logging.config


log_file_name = os.path.join(os.getcwd(), 'log.txt')
conf = {
    'filename': log_file_name,
    'level': logging.DEBUG,
    'filemode': 'a',
    'format': '%(asctime)s - %(name)s - %(levelname)s: %(message)s',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(module)s[%(levelname)s][%(asctime)s][p_%(process)d][t_%(thread)d]: %(message)s'
        },
        'simple': {
            'format': '%(module)s[%(levelname)s]: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': log_file_name,
        },
    },
    'loggers': {
        __name__: {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


def main():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formater = logging.Formatter(conf['format'])

    fh = logging.FileHandler(conf['filename'])
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formater)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formater)

    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger


if __name__ == '__main__':
    name = 'wenshin'
    # logger = main()
    logging.config.dictConfig(LOGGING)
    logger = logging.getLogger(__name__)
    logger.debug('I am a log %s' % name)
    logger.error('I am a log %s' % name)
