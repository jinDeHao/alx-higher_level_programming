#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = len(my_list) - 1
    if my_list != None:
        while i >= 0:
            print("{:d}".format(my_list[i]))
            i -= 1