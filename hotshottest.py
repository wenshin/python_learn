#!/usr/bin/env python
# encoding: utf-8
# by wenshin

import hotshot
import hotshot.stats
# hotshot is deprected


def runten():
    for n in xrange(10000):
        n = n * 2


def runone():
    for n in xrange(1000):
        n = n * 2


p = hotshot.Profile('test.prof')
p.start()

runten()

p.stop()

runone()

p.start()

runten()

p.close()

stats = hotshot.stats.load("test.prof")
stats.strip_dirs()
stats.sort_stats('time', 'calls')
stats.print_stats(20)


import cProfile, pstats, StringIO
pr = cProfile.Profile()
pr.enable()

# doing something
pr.disable()
s = StringIO.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print s.getvalue()
