"""
Task:
    You are given a string  and width .
    Your task is to wrap the string into a paragraph of width .

Function Description
    Complete the wrap function in the editor below.

    wrap has the following parameters:
        string string: a long string
        int max_width: the width to wrap to

Returns
    string: a single string with newline characters ('\n') where the breaks should be

Input Format
    The first line contains a string, string.
    The second line contains the width, max_width.

Constraints
    0 < len(string) < 1000
    0 < max_width < len(string)
"""

import textwrap

def wrap(string, max_width) -> str:
     return ("\n".join(textwrap.wrap(string, width=max_width)[0:]))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)