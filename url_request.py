#!/usr/bin/env python
# encoding: utf-8
# by wenshin

import gevent
from gevent import monkey
monkey.patch_all()

import requests
import urllib2
import urllib3
from multiprocessing import Pool, Process


def worker(url, url_type=None):
    if url_type == 'urllib2':
        content = urllib2.urlopen(url).read().lower()
    elif url_type == 'requests':
        content = requests.get(url).content.lower()
    elif url_type == 'urllib3':
        http = urllib3.PoolManager()
        content = http.request('GET', url).data.lower()
    title = content.split('<title>')[1].split('</title>')[0].strip()
    print title
    if not title:
        print 'Parse html error!'


num = 5
urls = ['http://www.baidu.com'] * num
print "urls = ['http://www.baidu.com'] * ", num


def url_gevent(url_type):
    lurls = urls * 5
    jobs = [gevent.spawn(worker, url, url_type) for url in lurls]
    gevent.joinall(jobs)


def gevent_process(urls):
    jobs = [gevent.spawn(worker, url, 'requests') for url in urls]
    gevent.joinall(jobs)
    return urls


POOL_SIZE = 5
# Process Pool is not right
def url_progress(url_type, poolsize=POOL_SIZE):
    pool = []
    if len(pool) < poolsize:
        p = Process(target=gevent_process, args=())
    q = pool.map(gevent_process, [urls]*5)


def url_pure(url_type):
    for url in iter(urls):
        worker(url, url_type)


if __name__ == '__main__':
    import time
    from timeit import Timer

    # requests
    # t = Timer(stmt="url_gevent('requests')",
    #           setup="from __main__ import url_gevent")
    # print 'by requests with gevent: %s seconds' % t.timeit(number=1)


    start = time.time()
    url_progress('requests')
    stop = time.time()
    print '>>> consume: ', (stop - start)

    # t = Timer(stmt="url_pure('requests')",
    #           setup="from __main__ import url_pure")
    # print 'by requests pure: %s seconds' % t.timeit(number=1)

    # # urllib3
    # t = Timer(stmt="url_gevent('urllib3')",
    #           setup="from __main__ import url_gevent")
    # print 'by urllib3 with gevent: %s seconds' % t.timeit(number=1)

    # t = Timer(stmt="url_pure('urllib3')",
    #           setup="from __main__ import url_pure")
    # print 'by urllib3 pure: %s seconds' % t.timeit(number=1)

    # # urllib2
    # t = Timer(stmt="url_gevent('urllib2')",
    #           setup="from __main__ import url_gevent")
    # print 'by urllib2 with gevent: %s seconds' % t.timeit(number=1)

    # t = Timer(stmt="url_pure('urllib2')",
    #           setup="from __main__ import url_pure")
    # print 'by urllib2 pure: %s seconds' % t.timeit(number=1)
