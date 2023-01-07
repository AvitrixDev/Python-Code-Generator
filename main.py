# CODE GENERATOR

import random
from chars import char


def convert(string):
    li = list(string.split(" "))
    return li


convert(char)

print("This is a code generator. Please enter the amount of characters you would like to input. Remember, max is 10 Characters")

char_var = input("Characters: ")

if char_var == "10":
    char_length = [0] * 10
elif char_var == "9":
    char_length = [0] * 9
elif char_var == "8":
    char_length = [0] * 8
elif char_var == "7":
    char_length = [0] * 7
elif char_var == "6":
    char_length = [0] * 6
elif char_var == "5":
    char_length = [0] * 5
elif char_var == "4":
    char_length = [0] * 4
elif char_var == "3":
    char_length = [0] * 3
elif char_var == "2":
    char_length = [0] * 2
elif char_var == "1":
    char_length = [0] * 1

i = 0

new_code = []

while i < len(char_length):
    newChar = random.choice(char)
    new_code.append(newChar)
    i = i + 1


def listToString(s):
    # initialize an empty string
    str1 = ''

    # return string
    return (str1.join(s))


print(listToString(new_code))
