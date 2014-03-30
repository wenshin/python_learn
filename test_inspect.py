#!/usr/bin/env python
# encoding: utf-8
# by wenshin

# from inspect import getsource


abc = None
s = """
def abc(a):
    print a
"""
# s = "def abc(a):\n    print a"

print s

# def abc(a):
#     print a
# s = getsource(abc)
# print type(s), ':', s

exec s

print type(abc), abc
abc(1)
