#!/usr/bin/python3
import sys


def shrink(s):
    print(s[:8])


def enlarge(s):
    if len(s) < 8:
        print(s + "Z" * (8 - len(s)))
    else:
        print(s)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("none")
    else:
        for param in sys.argv[1:]:
            if len(param) > 8:
                shrink(param)
            elif len(param) < 8:
                enlarge(param)
            else:
                print(param)
