#/bin/python3
#-*- coding: utf-8 -*-


classmates = ['Michael', 'Bob', 'Trach']
print (classmates)
print("clamates[0]",classmates[0]);
print("clamates[0]",classmates[-1]);

print ('len(classmates)', len(classmates))
classmates.append("Adam")
print ('len(classmates)', len(classmates))

classmates.insert(1,"Jack")
print("clasmates insert", classmates)

L = [
    ['Apple', 'Google','Microsoft'],
    ['Java', 'Python','Ruby','PHP'],
    ['Adam', 'Bart','Lisa','PHP'],
    ]

print(L[0][0])
print(L[1][1])
print(L[2][2])

print(len(L))
print(len(L[0]))
print(len(L[0][0]))
