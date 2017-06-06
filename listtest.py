# -*- coding:utf-8 -*-

L = [
        ['Apple', 'Google', 'Microsoft'],
        ['Java','Python','Ruby','PHP'],
         ['Adam','Bart','Lisa']
    ]

print(L[0][0])
print(L[1][1])
print(L[2][2])

L[0][1] = 'Amazon'
print(L[0])
print(L[0][0])
print(L[0][1])
print(L[0][2])
print(L[1][0])
L.pop(1)
print(L[1])
L.append('China')
print(L[len(L)-1])

