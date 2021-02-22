#!/usr/bin/env python
# -*- coding:utf8 -*-

# @author: Yuan
# @file: section_0.py
# @date: 2021-01-12

"""
以点号访问属性为例（obj.attr），Python 解释器会调用 __getattr__ 和 __setattr__ 计算属性。
如果 obj.no_such_attr，但我们在 __getattr__ 里面做了相应的处理的话，也能正确返回。
这个重写操作貌似就实现了动态属性的功能。

参考讨论：https://stackoverflow.com/questions/4295678/understanding-the-difference-between-getattr-and-getattribute
"""

class DynamicAttr:

    def __getattr__(self, item):
        """这个方法只会在 __getattribute__ 找不到的时候才会调用
        __getattribute__ 这个永远都会调用
        """
        print(f"__getattr__: {item}")
        if item == "abc":
            return "OH!"
        # getattr is a built-in function. getattr(foo, 'bar') is equivalent to foo.bar also is equivalent to foo.__getattribute__('bar')
        # getattr(foo, 'bar') == foo.bar == foo.__getattribute__('bar')
        return getattr(self, item)

    def __getattribute__(self, item):
        print(f"__getattribute__: {item}")
        return super(DynamicAttr, self).__getattribute__(item)


if __name__ == '__main__':
    da = DynamicAttr()

    """
    da.xyz = "123"
    print(da.abc)
    print(da.xyz)
    
    >>>
    __getattribute__: abc
    __getattr__: abc
    OH!
    __getattribute__: xyz
    123
    """

    """
    # da.xyz = "123"
    print(da.abc)
    print(da.xyz)

    >>>
    __getattribute__: abc
    __getattr__: abc
    OH!
    __getattribute__: xyz
    __getattr__: xyz
    __getattribute__: xyz
    __getattr__: xyz
    __getattribute__: xyz
    __getattr__: xyz
    __getattribute__: xyz
    __getattr__: xyz
    RecursionError: maximum recursion depth exceeded while calling a Python object
    """
