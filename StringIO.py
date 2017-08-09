#!/usr/bin python3
#-*- coding:utf-8 -*-

from io import StringIO

f = StringIO()
f.write("hello StringIO")

print(f.getvalue())
