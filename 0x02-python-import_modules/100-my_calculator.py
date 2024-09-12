#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    # Ensure correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Extract and convert arguments
    first_operand = int(sys.argv[1])
    operator = sys.argv[2]
    second_operand = int(sys.argv[3])

    # Calculate result based on operator
    if operator == '+':
        result = add(first_operand, second_operand)
    elif operator == '-':
        result = sub(first_operand, second_operand)
    elif operator == '*':
        result = mul(first_operand, second_operand)
    elif operator == '/':
        result = div(first_operand, second_operand)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Output the calculation
    print(f"{first_operand} {operator} {second_operand} = {result}")
