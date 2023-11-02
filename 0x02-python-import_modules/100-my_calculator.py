#!/usr/bin/python3
if __name__ == "__main__":
    """
    Makes basic arithmatic on cmd line args

    """
    from calculator_1 import add, mul, sub, div
    from sys import argv, exit
    if len(argv) != 4:
        print("Usage./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op = {"+": add, "-": sub, "*": mul, "/": div}
    if argv[2] in op:
        a = int(argv[1])
        b = int(argv[3])
        print("{} {} {} = {op[argv[2]](a, b)}".format(a, argv[2], b))
    else:
        print(f"Unknown operator. Available operators: +, -, * and /")
