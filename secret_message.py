from random import randint

alphabet = 'abcdefghijklmnopqrstuvwxyz'


new_message = ""
message = input("Please enter a string: ")


def changestring(string):
    global new_message
    for char in string:
        key = randint(0, 25)
        position = alphabet.find(char)
        new_position = (position + key)%26
        new_char = alphabet[new_position]
        print("The new char is: " + new_char)
        new_message += new_char
changestring(message)
print(new_message)
