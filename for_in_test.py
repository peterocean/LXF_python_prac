#/bin/bash python3
#-*- coding:utf-8 -*-


sum = 0
for x in [1,2 ,3,4, 5,6,7,8,9,10]:
    sum = sum +x
print("sum", sum)

sum = 0
for x in range(101):
    sum = sum + x
print("sum",sum)

#while test
print("while test:")

sum = 0
n = 99

while n > 0:
    sum += n
    n -= 2
print(sum)


L = ["Bart", "Lisa", "Adam"]
for name in L:
    print("Hello, ",name,"!")

print("break test")
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n += 1
print("End")

print("continue test \n")

n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    print(n)
print("End")

