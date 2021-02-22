#!/usr/bin/env python
# -*- coding:utf8 -*-

# @author: Yuan
# @file: section_1.py
# @date: 2021-01-12

import json
import keyword

with open("example.json", encoding='UTF-8') as fp:
    feed = json.load(fp)


# feed['Schedule']['events'][40]['name']

from collections import abc
# class FrozenJSON:
#     """一个只读接口，使用属性表示法访问JSON类对象 """
#     def __init__(self, mapping):
#         self.__data = dict(mapping)
#
#     def __getattr__(self, name):
#         if hasattr(self.__data, name):
#             return getattr(self.__data, name)
#         else:
#             return FrozenJSON.build(self.__data[name])
#
#     @classmethod
#     def build(cls, obj):
#         if isinstance(obj, abc.Mapping):
#             return cls(obj)
#         elif isinstance(obj, abc.MutableSequence):
#             return [cls.build(item) for item in obj]
#         else:
#             return obj

# class FrozenJSON:
#     """一个只读接口，使用属性表示法访问JSON类对象 """
#     def __init__(self, mapping):
#         self.__data = {}
#         for key, val in mapping.items():
#             if keyword.iskeyword(key):
#                 key = f"{key}_"
#             self.__data[key] = val
#
#     def __getattr__(self, name):
#         if hasattr(self.__data, name):
#             return getattr(self.__data, name)
#         else:
#             return FrozenJSON.build(self.__data[name])
#
#     @classmethod
#     def build(cls, obj):
#         if isinstance(obj, abc.Mapping):
#             return cls(obj)
#         elif isinstance(obj, abc.MutableSequence):
#             return [cls.build(item) for item in obj]
#         else:
#             return obj


class FrozenJSON:
    """一个只读接口，使用属性表示法访问JSON类对象"""

    def __init__(self, mapping):
        self.__data = dict(mapping)  # 确保 __data 是一个字典 & 安全起见复制 mapping 数据(浅拷贝)

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON(self.__data[name])

    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super(FrozenJSON, cls).__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg


class MyClass:
    def __init__(self, *args, **kwargs):
        print(f"__init__.args: {args}")
        print(f"__init__.kwargs: {kwargs}")

    def __new__(cls, *args, **kwargs):
        print(f"__new__.args: {args}")
        print(f"__new__.kwargs: {kwargs}")
        # return cls("哈哈", user_id="a")
        return super(MyClass, cls).__new__(cls)


if __name__ == '__main__':
    # fj = FrozenJSON(feed)
    # print(fj.Schedule.events[0].name)

    mc = MyClass(1, 2, 3, a='a', b='b')

