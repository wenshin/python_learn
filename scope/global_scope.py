#!/usr/bin/env python
# encoding: utf-8


# var1 = 1
# var2 = 2
# print var1, var2, 'outside'


def top_f():
    var = {'var1': 0, 'var2': 0}
    print var['var1'], var['var2'], 'top in'

    def nest_f():
        print var['var1'], var['var2'], 'nest in before assign'
        var['var1'] += 1
        var['var2'] += 2
        print var['var1'], var['var2'], 'nest in after assign'
    nest_f()

top_f()
