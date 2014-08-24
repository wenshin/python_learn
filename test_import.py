#!/usr/bin/env python
# encoding: utf-8
# by wenshin

from types import ClassType


m = __import__('cls', fromlist=('*'))
A = m.A
# ASon = getattr(a, 'ASon')
print A, 'get A class'
print dir(A)
print A.__module__
# print ASon, type(ASon), 'get ASon class'
# print issubclass(ASon, A), 'judgement'
