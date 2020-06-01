# This program calculates y = x|k,
# Warning:
# There is no timeout so be careful what you pass it

import argparse


def calc(x, k):  # calculate y = x|k
    y = 1
    if k >= 1:
        y = x ** calc(x, k - 1)
    return y


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("x", type=int, nargs='?', const=0)
    parser.add_argument("k", type=int, nargs='?', const=0)
    args = parser.parse_args()
    if args.k is None:
        args.x = int(input("x:"))
        args.k = int(input("k:"))
    print(calc(args.x, args.k))


if __name__ == "__main__":
    main()
