#Python Banking Program

def show_balance():
    print(f"Your current balance is: ${balance}")

def deposit():
    global balance#THis gloabl keyword is used to point at the global variable balance
    depo_amt = float(input("Enter the amount to deposit: "))
    balance += depo_amt
    print(f"Successfully deposited ${depo_amt}")

def withdraw():
    global balance
    withdraw_amt = float(input("Enter the amount to withdraw: "))
    if withdraw_amt > balance:
        print("Insufficient funds. Withdrawal failed.")
    else:
        balance -= withdraw_amt
        print(f"Successfully withdrew ${withdraw_amt}")

balance = 0

while True:
    print("***** Welcome to the Banking Program *****")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    match choice:
        case 1:
            show_balance()
        case 2:
            deposit()
        case 3:
            withdraw()
        case 4:
            print("Thank you for using the Banking Program!")
            break
        case _:
            print("Invalid choice. Please try again.")