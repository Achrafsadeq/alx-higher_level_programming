#!/usr/bin/python3
# Ensure this block runs only when the script is executed directly
if __name__ == "__main__":
    # Import all necessary functions from calculator_1.py
    from calculator_1 import add, sub, mul, div

    a = 10  # Assign the value 10 to variable a
    b = 5   # Assign the value 5 to variable b

    # Perform each operation and print the result
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
