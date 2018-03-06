#!/usr/bin python3
#-*- coding:utf-8 -*-

def foo(s):
    n = (int)(s)
    assert(n != 0), 'n is zero'
    return 10/n

def main():
    foo(5)
    foo(1)

print(foo(5))
print(foo(0))

