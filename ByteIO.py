#!/usr/bin python3
#-*- coding:utf-8 -*-

from io import BytesIO

f = BytesIO()
f.write('中文'.encode('utf-8'))

print(f.getvalue())
