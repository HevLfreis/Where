#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com 
# Date: 2017/3/2
# Time: 22:27
from core import cache


# cache decorator
def get_or_set(kw, timeout=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            arg = '-'.join(map(str, args))
            key = kw + '-' + arg
            data = cache.get(key)
            if not data:
                # print key, 'notin'
                data = func(*args, **kwargs)
                if timeout:
                    cache.set(key, data, timeout)
                else:
                    cache.set(key, data)
            # else:
            #     print key, 'bingo'
            return data
        return wrapper
    return decorator
