#!/usr/bin/python3
if __name__ == "__main__":
    """
    Makes basic arithmatic on cmd line args

    """
    from calculator_1 import add, mul, sub, div
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    op = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] in op:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        print("{} {} {} = {}".format(a, sys.argv[2], b, op[sys.argv[2]](a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
