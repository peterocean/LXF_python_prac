#!/usr/bin/env python3

type(123)
print(type(123))

class MyObject(object):
    def __init__(self):
        self.x = 9;
    def power(self):
        return self.x*self.x
    def __len__(object):
        return 100
obj = MyObject()

print(hasattr(obj,'x'))

print(hasattr(obj,'y'))
print(len(obj))
