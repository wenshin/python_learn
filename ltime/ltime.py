#!/usr/bin/env python
# encoding: utf-8
# by wenshin

import time
from datetime import datetime
from dateutil import parser


def ISODate2TimeStamp(date_str):
    dt = parser.parse(date_str)
    ts = time.mktime(dt.timetuple())
    return ts


def fromtimestamp(timestamp):
    return datetime.fromtimestamp(float(timestamp))


if __name__ == '__main__':
    import sys
    date_str = sys.argv[1]
    print ISODate2TimeStamp(date_str)
