#Hangman game in python
import random

words = (
    # Fruits & Food
    "apple", "orange", "banana", "coconut", "pineapple", "strawberry", 
    "blueberry", "watermelon", "avocado", "pomegranate", "pancake", 
    "spaghetti", "chocolate", "sandwich", "croissant",

    # Animals
    "elephant", "giraffe", "kangaroo", "chameleon", "flamingo", 
    "octopus", "cheetah", "hedgehog", "alligator", "penguin", 
    "platypus", "dolphin", "rhinoceros", "chimpanzee", "hippopotamus",

    # Tech & Science
    "python", "computer", "algorithm", "keyboard", "database", 
    "software", "hardware", "internet", "dinosaur", "telescope", 
    "microscope", "laboratory", "molecule", "astronomy", "velocity",

    # Places & Nature
    "mountain", "waterfall", "volcano", "glacier", "blizzard", 
    "rainforest", "canyon", "archipelago", "desolation", "horizon", 
    "continent", "wilderness", "monument", "lighthouse", "sanctuary",

    # Objects & Everyday Things
    "umbrella", "backpack", "binoculars", "headphones", "telescope", 
    "chandelier", "sundial", "hourglass", "kaleidoscope", "compass",

    # Verbs & Adjectives (Trickier guesses)
    "mysterious", "whimsical", "adventure", "puzzle", "labyrinth", 
    "symphony", "whisper", "avalanche", "phantom", "paradox", 
    "quicksand", "vortex", "blizzard", "treacherous", "serendipity",
)

hangman_art = { 
    0: (
        "  +---+",
        "  |   |",
        "      |",
        "      |",
        "      |",
        "      |",
        "=========",
    ),
    1: (
        "  +---+",
        "  |   |",
        "  O   |",
        "      |",
        "      |",
        "      |",
        "=========",
    ),
    2: (
        "  +---+",
        "  |   |",
        "  O   |",
        "  |   |",
        "      |",
        "      |",
        "=========",
    ),
    3: (
        "  +---+",
        "  |   |",
        "  O   |",
        " /|   |",
        "      |",
        "      |",
        "=========",
    ),
    4: (
        "  +---+",
        "  |   |",
        "  O   |",
        " /|\\  |",
        "      |",
        "      |",
        "=========",
    ),
    5: (
        "  +---+",
        "  |   |",
        "  O   |",
        " /|\\  |",
        " /    |",
        "      |",
        "=========",
    ),
    6: (
        "  +---+",
        "  |   |",
        "  O   |",
        " /|\\  |",
        " / \\  |",
        "      |",
        "=========",
    ),
}

def display_man(wrong_guesses):
    for i in hangman_art[wrong_guesses]:
        print(i)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print("The word was:",answer)

def main():
    answer = random.choice(words)
    hint = ["_"]*len(answer)
    wrong_guesses = 0
    is_running = True
    flag = False

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input..")
            continue

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1        

        if wrong_guesses == 6:
            flag = False
            break
        elif "".join(hint) == answer:
            flag = True
            break
    
    if flag:
        print("You got the word!!")
    elif not flag:
        print("Sorry! you didn't get to word...")

    display_answer(answer)
        

if __name__ == "__main__":
    main()
        
