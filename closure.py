#!/usr/bin/env python
# encoding: utf-8


def fun():
    num = {'a': 1}

    def in_fun():
        a = num
        a['b'] = 1
        print '>>> a: ', a

    in_fun()
    print '>>> num: ', num

fun()
# python 闭包变量不能直接进行赋值，只能通过赋值给新变量改变
