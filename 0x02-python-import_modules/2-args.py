#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv) - 1

    if i == 0:
        print("{} argumants.".format(i))
    elif i == 1:
        print("{} argumant:".format(i))
    else:
        print("{} argumants:".format(i))

        if i >= 1:
            i = 0
            for arg in sys.argv:
                if i != 0:
                    print("{}: {}".format(i, arg))
                    i += 1
