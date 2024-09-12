#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, subtract, multiply, divide
    import sys

    # Verify the script has exactly three arguments plus the script name
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Convert command-line arguments to integers and operator
    num1 = int(sys.argv[1])
    op = sys.argv[2]
    num2 = int(sys.argv[3])

    # Determine the operation to perform based on the operator
    if op == '+':
        outcome = add(num1, num2)
    elif op == '-':
        outcome = subtract(num1, num2)
    elif op == '*':
        outcome = multiply(num1, num2)
    elif op == '/':
        outcome = divide(num1, num2)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Output the result in the required format
    print(f"{num1} {op} {num2} = {outcome}")
