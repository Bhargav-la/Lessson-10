from abc import ABC, abstractmethod

class animal(ABC):
    def move(self):
        pass

class Human(animal):
    def move(self):
        print("I can walk and run")

class Snake(animal):
    def snake(self):
        print("I can crawl")

class Dog(animal):
       def move(self):
           print("I can roar")

class Lion(animal):
    def move(self):
        print("I can roar")

R = Human()
R.move()

K = Snake()
K.move()

L = Dog()
L.move()

A = Lion()
A.move()
       
