#-*- coding:utf-8 -*-

def enroll(name,gender,age=18,city='Beijing'):
    print('name',name)
    print('gener',gender)
    print('age', age)
    print('city',city)


enroll('Sarah','F')
enroll('peter','M')
enroll('charlie','M',23)
enroll('Lucy','F',city = 'Shenzhen')
