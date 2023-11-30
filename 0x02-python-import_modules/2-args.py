#!/usr/bin/python3
#  Prints num and list of its args
if __name__ == "__main__":
    import sys

    arg = sys.argv
    s = len(arg) - 1

    if s > 1:
         print("{} arguments:".format(s))
        for i in range(1, s + 1):
            print("{}: {}".format(i, arg[i]))

    elif s == 0:
        print("{} arguments.".format(s))

    else:
        print("{} argument:".format(s))
        print("{}: {}".format(s, arg[1]))
