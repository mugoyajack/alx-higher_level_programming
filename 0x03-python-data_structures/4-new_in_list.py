#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 1 or idx > len(my_list):
        return my_list
    else:
        new_list = []
        new_list = [num for num in my_list]
        new_list[idx] = element
        return new_list