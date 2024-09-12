#!/usr/bin/python3
if __name__ == "__main__":
    # Import the add function from the file add_0.py
    from add_0 import add
    
    a = 1 
    b = 2
    # Print the result of the addition using formatted string
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
