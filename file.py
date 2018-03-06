#!/usr/bin  python3
#-*- coding:utf-8 -*-


f = open('test.txt','w')
f.write('hello text.txt!')
f.close

f = open('test.txt','r')
print(f.read())
f.close()


with open('test.txt','w') as f:
    f.write('hello world')
