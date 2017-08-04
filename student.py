#!/usr/bin/env python3
# -*- coding:utf-8 -*_

class Student(object):
    def __init__(self):
        self.__score = 0
    def get_score(self):
        return self.__score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError("score must be intger!")
        if value < 0 or value > 100:
            raise ValueError("score must between 0~100!")
        self.__score = value
        
    @property
    def birth(self):
        return self.__birth
    @birth.setter
    def birth(self,value):
        self.__birth = value

    @property
    def age(self):
        return 2015-self.__birth
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,new_name):
        if not isinstance(new_name,str):
            raise ValueError("name must be string!")
        self.__name = new_name
    @name.getter
    def name(self):
        return self.__name
    
s = Student()
s.name = "peter yang"
print(s.name)
print(s.get_score())
s.set_score(60)
print(s.get_score())
s.name = 60

                             
