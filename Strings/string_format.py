"""
Task
    Given an integer, , print the following values for each integer  i from 1  to n :
        Decimal
        Octal
        Hexadecimal (capitalized)
        Binary

Function Description
    Complete the print_formatted function in the editor below.

    print_formatted has the following parameters:
        int number: the maximum value to print
Prints
    The four values must be printed on a single line in the order specified above for each i from 1 to number.
    Each value should be space-padded to match the width of the binary value of number and the values should be separated by a single space.

Input Format
    A single integer denoting n.

Constraints
    1 <= n <= 99
"""

def print_formatted(number: int):
    # to store each line
    lines = []
    # to store width of binary #
    width: int = 0
    for x in range(1,n+1):
        # doesn't matter since the last binary # will be the biggest
        width: int = len(bin(x)[2:])
        # add each representation/formatted number as a line to lines
        lines.append([x, oct(x)[2:], hex(x)[2:].upper(), bin(x)[2:]])

    # for each line in lines
    for line in lines:
        # print right alligned (based on larget binary value length) formatted number
        print(*(str(formatted_number).rjust(width) for formatted_number in line))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)