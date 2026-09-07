#Python slot machine game
import random
def spin_row():
    symbols = ["🍒", "🍋", "🍊", "🍉", "🍇"]

    results =[random.choice(symbols) for i in range(3)]
    
    return results

def print_row(row):
    print(" | ".join(row))

def pay_out(row, bet):
    if row[0] == row[1] == row[2]:
        print(f"Congratulations! You won ${bet * 10}!!")
        return bet * 10
    elif row[0] == row[1] or row[1] == row[2] or row[0] == row[2]:
        print(f"You won ${bet * 2}!")
        return bet * 2
    else:
        print("Sorry, you lost the bet..")
        return 0
    

def main():
    balance = 100
    print("***** Welcome to the Slot Machine Game *****")
    print("Symbols: 🍒 🍋 🍊 🍉 🍇")
    print("------------------------------------------------")

    while balance > 0:
        bet = input(f"Enter the amount of money you want to bet (Current balance: ${balance}): ")
        if not bet.isdigit():
            print("Please enter a valid number.")
            continue

        bet = int(bet)
        if bet > balance:
            print("Insufficient balance. Please enter a valid bet amount.")
            continue
        elif bet <= 0:
            print("The bet amount must be greater than zero.")
            continue

        balance -= bet
        row = spin_row()
        print_row(row)
        balance += pay_out(row, bet)

        print(f"Do you want to play again? (y/n):")
        choice = input().lower()
        if choice == 'n':
            print(f"Thank you for playing! Your final balance is: ${balance}")
            break
        elif choice == 'y':
            continue
        else:
            print("Invalid choice. Exiting the game.")
            break

if __name__ == "__main__":
    main()