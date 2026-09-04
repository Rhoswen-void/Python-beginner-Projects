import math as m

def square_root(num):
    return m.sqrt(num)

def square(num):
    return m.pow(num,2)

def cube(num):
    return m.pow(num,3)

def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact

while True:
    print("=========MENU=========")
    print("1. Square root of a number")
    print("2. Square of a number")
    print("3. Cube of a number")
    print("4. Factorial of a number")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            num = float(input("Enter a number: "))
            print(f"Square root of {num} is {square_root(num)}")
        case 2:
            num = float(input("Enter a number: "))
            print(f"Square of {num} is {square(num)}")
        case 3:
            num = float(input("Enter a number: "))
            print(f"Cube of {num} is {cube(num)}")
        case 4:
            num = int(input("Enter a number: "))
            print(f"Factorial of {num} is {factorial(num)}")
        case 5:
            print("Exiting...")
            break
        case _:
            print("Invalid choice. Please try again.")