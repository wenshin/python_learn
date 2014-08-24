#!/usr/bin/env python
# encoding: utf-8
# by wenshin


def func(fn):
    fn()


abc = 123333


def callback():
    print abc


func(callback)
