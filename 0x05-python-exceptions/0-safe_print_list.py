#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0
    for n in range(x):
        try:
            print("{:d}".format(my_list[n]), end="")
            c += 1
        except (IndexError):
            break
    print()
    return c
