#!/usr/bin/env python3
#-*- coding:utf-8 -*-

class Student(object):
    
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    pass
    
    def print_score(self):
        print('%s:%s' %(self.__name, self.__score))

bart = Student('Bart Simpson', 98)
bart.print_score()
