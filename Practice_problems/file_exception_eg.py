#Python file detection

import os

file_path = r"Documentation\Infos" #r before the quote tells the python compiler to take backlash escape sequences as normal string chars

if os.path.exists(file_path):
    print(f"The location of '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file.")
    elif os.path.isdir(file_path):
        print("That is a directory.")
else:
    print("That location doesn't exist")