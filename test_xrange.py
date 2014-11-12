#!/usr/bin/env python
# encoding: utf-8

import time


@profile
def fn1(data, step=10):
    for i in xrange(len(data)):
        yield data[i*step:(i+1)*step]


@profile
def fn2(data, step=10):
    for i in xrange(0, len(data), step):
        yield data[i: i+step]


if __name__ == '__main__':
    data = [1*1000000]
    print data
    t1 = time.time()
    fn1(data)
    t2 = time.time()
    print t1
    print t2

    t1 = time.time()
    fn2(data)
    t2 = time.time()
    print t1
    print t2
