#/bin/bash python3
#-*- coding:utf-8 -*--

d = { 'Michael':96, 'Bob':75, 'Tracy':85}
print(len(d))

for key in d.keys():
    print(key)
    print(d[key])


for value in d.values():
    print(value)
