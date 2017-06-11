#-*- coding:utf-8 -*-


import math
def quadratic(a,b,c):
    f1 = (-b + math.sqrt(b*b - 4*a*c)) / (2*a)
    f2 = (-b - math.sqrt(b*b - 4*a*c)) / (2*a)
    return f1,f2

print(quadratic(2,3,1))
print(quadratic(1,3,-4))
