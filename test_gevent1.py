#!/usr/bin/env python
# encoding: utf-8
# by wenshin

import gevent
from gevent import monkey
monkey.patch_socket()

from gevent.pool import Pool
from gevent.queue import Queue

import threading
import requests


def work(url):
    content = requests.get(url, timeout=1).content.lower()
    title = content.split('<title>')[1].split('</title>')[0].strip()
    print title, url
    return title


def main():
        worker1 = gevent.spawn(work, 'http://www.baidu.com')
        worker2 = gevent.spawn(work, 'http://www.baidu.com')
        print worker1.successful(), worker1.ready(), worker1.started, 111111111111
        print worker2.successful(), worker2.ready(), worker2.started, 111111111111
        worker1.join()
        worker2.join()
        print worker1.successful(), worker1.ready(), worker1.started, 222222222222
        print worker2.successful(), worker2.ready(), worker2.started, 222222222222


if __name__ == '__main__':
    from timeit import Timer
    main()
