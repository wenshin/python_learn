#!/usr/bin/env python
# encoding: utf-8
# by wenshin

import gevent
from gevent import monkey
monkey.patch_socket()

from gevent.pool import Pool
from gevent.queue import Queue

import requests


def work(url):
    content = requests.get(url, timeout=10).content.lower()
    title = content.split('<title>')[1].split('</title>')[0].strip()
    print title, url
    return title


def work_input_file(urls, results, reader):
    while urls.qsize() > 0 or not reader.successful():
        url = urls.get()
        title = work(url)
        results.put_nowait(title)


def readfile(filename, urls):
    with open(filename) as f:
        while 1:
            if urls.qsize() < 100:
                print 'reading_file'
                line = f.readline()
                if line:
                    urls.put_nowait(line[:-1])
                else:
                    break
            else:
                gevent.sleep(0)


def main(psize, filename=None):
    psize = int(psize)
    if filename:
        urls = Queue()
        results = Queue()
        reader = gevent.spawn(readfile, filename, urls)
        jobs = [gevent.spawn(work_input_file, urls, results, reader) for i in xrange(psize)]
        print jobs, 11111111111
        gevent.joinall(jobs)
        print results.qsize(), 3333333333333333333
        print urls.qsize(), 3333333333333333333
        return results
    else:
        pool = Pool(psize)
        urls = ['http://www.baidu.com'] * 100
        return pool.map(work, urls)


if __name__ == '__main__':
    import sys
    from timeit import Timer

    print sys.argv, '111111111111111'
    psize = sys.argv[1]
    filename = sys.argv[2] if sys.argv[2] else None
    print filename, '2222222222'
    t = Timer(stmt="main(psize, filename)",
              setup="from __main__ import main, psize, filename")
    print 'by requests with gevent: %s seconds' % t.timeit(number=1)
