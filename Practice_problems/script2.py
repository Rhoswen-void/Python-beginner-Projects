from script1 import *

def fav_drink(drink):
    print(f"Your favorite drink is {drink}")

print("This is the main function of script2.")
fav_food("sushi")
fav_drink("coffee")
print("Bye Bye!")

#so here we are running script2 but since we imported script1, it will also run script1's code
#Unless we use the if __name__ == '__main__': guard in script1, it will execute the code in script1 when we import it here.