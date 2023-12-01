#!/usr/bin/python3
#  Prints num and list of its args
if __name__ == "__main__":
    import sys

    count = len(sys.arg) - 1
    if count == 0:
         print("0 arguments:")
    elif count == 1:
        print("1 arguments.")

    else:
        print("{} argument:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.arg[i + 1]))
