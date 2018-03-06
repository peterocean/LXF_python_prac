#!/usr/bin/env python3

class Animal(object):
    def run(self):
        print('Animal is running...')
    def run_twice(animal):
        animal.run()
        animal.run()

class  Dog(Animal):
    def run(self):
        print('Dog is running...')
    pass

class Cat(Animal):
    def run(self):
        print('Cat is runing');
    pass

dog = Dog();
dog.run()
cat = Cat();
cat.run();

run_twice(dog)

print(isinstance(cat,Cat));
print(isinstance(cat,Animal));
