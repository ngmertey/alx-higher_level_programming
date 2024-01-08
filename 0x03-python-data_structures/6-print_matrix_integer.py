#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for num1 in range(len(matrix)):
        for num2 in range(len(matrix[i])):
            print("{:d}".format(matrix[num1][num2]), end="")
                if num2 != (len(matrix[num1]) - 1):
                    print(" ", end="")

        print("")
