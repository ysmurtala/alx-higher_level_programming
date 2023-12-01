#!/usr/bin/python3
#  Prints num and list of its args
if __name__ == "__main__":
    import sys

    s = len(sys.arg) - 1
    if s == 0:
         print("0 arguments:")
    elif s == 1:
        print("1 arguments.")

    else:
        print("{} argument:".format(s))
    for i in range(s):
        print("{}: {}".format(i + 1, sys.arg[i + 1]))
