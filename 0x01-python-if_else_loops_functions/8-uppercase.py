#!/usr/bin/python3
# Print a string in uppercase

def uppercase(str):
    """Print a string in uppercase."""
    for c in str:
# Check if the character is lowercase
        if ord(c) >= 97 and ord(c) <= 122:  
            c = chr(ord(c) - 32)  # Convert to uppercase
        print("{}".format(c), end="")
    print("")  
