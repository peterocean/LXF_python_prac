#!/usr/bin python3
#-*- coding:utf-8 -*-


try:
    print('try...')
    r=10/0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally...')
print('END')


try:
    print('try...')
    r = 10 / int('2')
    print('result:',r)
except ValueError as e:
    print('Value Error:',e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')




