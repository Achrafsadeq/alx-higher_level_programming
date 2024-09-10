#!/usr/bin/python3
# Loop through ASCII values for lowercase letters (97 to 122)
for letter in range(97, 123):

    if chr(letter) != 'q' and chr(letter) != 'e':
        print("{}".format(chr(letter)), end="")
