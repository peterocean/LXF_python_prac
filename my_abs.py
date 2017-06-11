#-*- coding:utf-8 -*-

def my_abs(x):
    if x >= 0:
        return x;
    else:
        return -x

num = -5
print('num:',num)
print('abs(num):',my_abs(num))
