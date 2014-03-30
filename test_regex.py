#!/usr/bin/env python
# encoding: utf-8
# by wenshin

import re


rname = r'if __name__\s?==\s?[\'\"]__main__[\'\"]:(\n.+$)+'
fname = 'def abc():    pass\n\nif __name__ == "__main__":\n    pass\n    pass'
# fn = re.sub(rname, '', fname, flags=re.M)
# print re.sub(rname, '', fname, flags=re.M)

exec(fname)
print abc
