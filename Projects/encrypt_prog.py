import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)
key = chars.copy()#used to make a copy of the original list of characters
random.shuffle(key)#shuffles the list of characters in the key list randomly so every time we
                   #run the program we get a different key for encryption and decryption    

def encrypt(plain_text):
    cipher_text = ""
    for char in plain_text:
        if char in chars:
            index = chars.index(char)
            cipher_text += key[index]

    return cipher_text

def decrypt(cipher_text):
    plain_text = ""
    for char in cipher_text:
        if char in chars:
            index = key.index(char)
            plain_text += chars[index]

    return plain_text

def main():
    print("****** Welcome to the Encryption Program ******")
    print("------------------------------------------------")

    while True:
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                plain_text = input("Enter the message to encrypt: ")
                cipher_text = encrypt(plain_text)
                print(f"Encrypted message: {cipher_text}")
            case 2:
                cipher_text = input("Enter the message to decrypt: ")
                plain_text = decrypt(cipher_text)
                print(f"Decrypted message: {plain_text}")
            case 3:
                print("Exiting the program...")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()