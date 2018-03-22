#/bin/bash python3
#-*- coding:utf-8 -*-

def add_end1(L = []):
    L.append('END')
    return L

def add_end2(L = None):
    if L is None:
        L = [];
    L.append('END')
    return L


def person(name,age, **kw):
    print('name', name, 'age', age, 'other', kw)


print(add_end1([1,2,3]))
print(add_end1([3,4,5]))
print(add_end1())
print(add_end1())

print(add_end2([1,2,3]))
print(add_end2([3,4,5]))
print(add_end2())
print(add_end2())

person('Michael', 30)
person('Bob', 35,city = 'Beijing')
person('Adam',45, gender = 'M', job = 'Engineer')
person('Lucy',25, gender = 'F')
