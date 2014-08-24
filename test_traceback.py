#!/usr/bin/env python
# coding: utf-8

import traceback


try:
    print a
except Exception, e:
    print str(e)
    traceback.print_exc()
