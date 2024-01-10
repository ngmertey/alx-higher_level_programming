#!/usr/bin/python3
def common_elements(set_1, set_2):
    """returns a set of common elements in two sets."""
    common_set = {element for element in set_1 if element in set_2}
    return common_set
