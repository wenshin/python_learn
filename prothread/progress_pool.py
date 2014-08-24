#!/usr/bin/env python
# encoding: utf-8
# by wenshin

import time
from multiprocessing import Pool


p = Pool(4)


def w(x):
    while 1:
        print 'sleeping', x
        time.sleep(1)


p.map(w, [1,2,3])