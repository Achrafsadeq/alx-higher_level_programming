#!/usr/bin/python3

# Loop through ASCII values for lowercase letters (97 to 122)
for letter in range(97, 123):
    # Convert the ASCII value to a character
    # Print the character if it is not 'q' or 'e'
    if chr(letter) != 'q' and chr(letter) != 'e':
        # Print the character without a newline at the end
        print("{}".format(chr(letter)), end="")
