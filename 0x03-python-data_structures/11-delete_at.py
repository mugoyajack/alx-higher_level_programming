#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < len(my_list) and idx > -1:
        list2 = []
        for n in range(len(my_list)):
            if n != idx:
                list2.append(my_list[n])
        return list2
    return my_list
