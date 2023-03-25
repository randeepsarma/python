import argparse
import sys


def calc(args):
    if args.o == "add":
        return args.x + args.y
    elif args.o == "substract":
        return args.x - args.y
    elif args.o == "multiply":
        return args.x * args.y
    elif args.o == "divider":
        return args.x / args.y


if __name__ == "__main__":
    # making an object
    parser = argparse.ArgumentParser()

    parser.add_argument("--x", type=float, default=1.0, help="Enter First Number")
    parser.add_argument("--y", type=float, default=3.0, help="Enter Second Number")
    parser.add_argument("--o", type=str, default="add", help="Utility for calculation")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))
# to run the program use:
# python main.py --x 7 --y 8 --o add
