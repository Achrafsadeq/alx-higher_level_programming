#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    # Ensure correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Extract and convert arguments
    num1 = int(sys.argv[1])
    op = sys.argv[2]
    num2 = int(sys.argv[3])

    # Calculate result based on operator
    if op == '+':
        result = add(num1, num2)
    elif op == '-':
        result = sub(num1, num2)
    elif op == '*':
        result = mul(num1, num2)
    elif op == '/':
        result = div(num1, num2)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Output the calculation
    print(f"{num1} {op} {num2} = {result}")
