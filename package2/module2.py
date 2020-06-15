#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from package1.module1 import test1


def test2():
    print("package2.module2 here")


def test2_1():
    print("\nin package2.module2")
    test1()
    print("")
