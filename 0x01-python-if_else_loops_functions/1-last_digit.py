#!/usr/bin/python3
import random

# Assign a random integer within the range of -10000 to 10000
number = random.randint(-10000, 10000)

# Compute the last digit of `number`, adjusting for negative values
if number < 0:
    last_digit = number % -10  
    # Use -10 to handle negative last digit calculation
else:
    last_digit = number % 10  
    # Use 10 for non-negative numbers

# Output the base message showing the number and its last digit
print(f"Last digit of {number} is {last_digit}", end=" ")

# Add an appropriate description based on the last digit's value
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
