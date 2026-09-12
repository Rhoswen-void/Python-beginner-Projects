from math import e
def func():
    print(e)
print(func())


#Basically before printing the variable we first look for its
#Local instance, if not found then we look for it in the enclosing function,
#if not found then we look for the global instance,
#and if still not found then we look for the built-in instance of the variable.