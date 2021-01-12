#!/usr/bin/env python
# -*- coding:utf8 -*-

# @author: Yuan
# @file: section_1.py
# @date: 2021-01-12

"""
以点号访问属性为例（obj.attr），Python 解释器会调用 __getattr__ 和 __setattr__ 计算属性。
如果 obj.no_such_attr，但我们在 __getattr__ 里面做了相应的处理的话，也能正确返回。
这个重写操作貌似就实现了动态属性的功能。
"""

class DynamicAttr:

    def __getattr__(self, item):
        return super(DynamicAttr, self).__getattr__(item)
