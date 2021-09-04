"""
Task
    You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

    For Example:

        Www.HackerRank.com → wWW.hACKERrANK.COM
        Pythonist 2 → pYTHONIST 2  

Function Description
    Complete the swap_case function in the editor below.
    swap_case has the following parameters:
    string s: the string to modify

Returns
    string: the modified string

Input Format
    A single line containing a string .

Constraints
    0 < len(s) < 1000
"""
def swap_case(s: str) -> str:
    swaped_string: str = ''
    for char in s:
        if char.islower():
            swaped_string += char.upper()
        elif char.isupper():
            swaped_string += char.lower()
        else:
            swaped_string += char
    return swaped_string

if __name__ == '__main__':
    s = 'HackerRank.com presents "Pythonist 2".'
    result = swap_case(s)
    print(result)