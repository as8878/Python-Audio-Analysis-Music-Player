# encoding: utf-8


# author: Ankit Singh
# email: singhanki67@gmail.com

import re 
import os  
import sys


class Struct():

    def __init__(self, **kwds):
        self.__dict__.update(kwds)

    def items(self):
        return self.__dict__.items()

    def values(self):
        return self.__dict__.values()

    def keys(self):
        return self.__dict__.keys()


def rename(ORIGINAL, SCRIPT, SYSPATH):
    sys.path = SYSPATH
    del SYSPATH
    try:
        for v in '__doc__|__file__|__name__|__package__'.split('|'):
            globals().pop(v)
        del v
    except Exception:
        pass
    KEYWORDS = ORIGINAL.keys()
    NEW = Struct()
    CUSTOMFIELD = ''
    for v in KEYWORDS:
        exec('%s = ORIGINAL.%s' % (v, v))
    del v
    try:
        exec(SCRIPT)
    except Exception:
        return
    NEW = Struct()
    for v in KEYWORDS:
        exec('NEW.%s = %s' % (v, v))
    del v
    NEW.CUSTOMFIELD = CUSTOMFIELD
    # print vars().keys()
    # print locals().keys()
    # print globals().keys()
    return NEW
