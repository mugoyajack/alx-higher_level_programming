#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not isinstance(my_list, list):
        return
    for num in my_list:
        print("{:d}".format(my_list[len(my_list) - num]))
