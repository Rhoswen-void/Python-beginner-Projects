def add_sprinkles(func):
    def wrapper(*args,**kwargs): #This function is required as it only executes the add_sprinkles function when the decorator 
        print("You add sprinkles 🧁")#Is called along with the get_icecream function, as we dont want it to execute 
                                     #Only by adding decorator
        func(*args,**kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args,**kwargs):# *args and **kwargs are used to pass any number of arguments in the function
        print("A fudge was added to your icecream 🍫")
        func(*args,**kwargs)
    return wrapper

@add_fudge
@add_sprinkles
def get_icecream(flavour):
    print(f"Here's your {flavour} ice cream 🍦")

get_icecream("Chocolate")

