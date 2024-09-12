#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    # Verify that the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <num1> <operator> <num2>")
        sys.exit(1)

    # Extract the command-line arguments
    num1 = int(sys.argv[1])
    op = sys.argv[2]
    num2 = int(sys.argv[3])

    # Determine and perform the requested arithmetic operation
    if op == '+':
        result = add(num1, num2)
    elif op == '-':
        result = sub(num1, num2)
    elif op == '*':
        result = mul(num1, num2)
    elif op == '/':
        result = div(num1, num2)
    else:
        print("Invalid operator. Supported operators: +, -, *, /")
        sys.exit(1)

    # Output the computed result in the desired format
    print(f"{num1} {op} {num2} = {result}")
