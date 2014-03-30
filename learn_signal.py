#!/usr/bin/env python
# encoding: utf-8
# by wenshin

import sys
import signal


def signal_handler(signal, frame):
    print('\nYou pressed Ctrl+C!')
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C')
signal.pause()
