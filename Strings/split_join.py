"""
Task
    You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen. Input Format
    The first line contains a string consisting of space separated words.

Function Description
    Complete the split_and_join function in the editor below.
    split_and_join has the following parameters:
    string line: a string of space-separated words

Returns
    string: the resulting string

Input Format 
    The one line contains a string consisting of space separated words.

Output Format
    Print the formatted string as explained above.
"""

def split_and_join(line: str) -> str:
    line: str = line.split(" ")
    return "-".join(line)
 
if __name__ == '__main__':
    line: str = input()
    result: str = split_and_join(line)
    print(result)