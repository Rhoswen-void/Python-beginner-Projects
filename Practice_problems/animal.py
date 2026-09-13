class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking!")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing!")

    def pur(self):
        print(f"{self.name} is purring.")
