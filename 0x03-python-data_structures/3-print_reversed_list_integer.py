#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for num in my_list:
        print("{0}".format(my_list[len(my_list) - num]))
