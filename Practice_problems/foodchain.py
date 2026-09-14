
class Animal:
    is_alive = True

    def sleep(self):
        print("This animal is sleeping")

    def eat(self):
        print("This animal is eating")

class Prey(Animal):
    def flee(self):
        print("This animal is fleeing")

class Predator(Animal):
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Predator,Prey):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

fish.flee()
fish.hunt()
fish.eat()
fish.sleep()