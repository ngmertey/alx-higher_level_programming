#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list


    copied_list = [i for i in my_list]
    copied_list[idx] = element
    return copied_list
