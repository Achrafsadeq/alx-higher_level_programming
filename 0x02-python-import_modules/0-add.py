#!/usr/bin/python3
if __name__ == "__main__":
    # Import the add function from the file add_0.py
    from add_0 import add
    
    a = 1  # Assign the value 1 to variable a
    b = 2  # Assign the value 2 to variable b
    
    # Print the result of the addition using formatted string
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
