"""
Task
    In this challenge, the user enters a string and a substring. 
    You have to print the number of times that the substring occurs in the given string. 
    String traversal will take place from left to right, not from right to left.
    NOTE: String letters are case-sensitive.

Input Format
    The first line of input contains the original string. The next line contains the substring.

Constraints
    1 <=len(string) <= 200
    Each character in the string is an ascii character.

Output Format
    Output the integer number indicating the total number of occurrences of the substring in the original string.

Concept
    Some string processing examples, such as these, might be useful. 
    There are a couple of new concepts: 
    In Python, the length of a string is found by the function len(s), where s is the string. 
    To traverse through the length of a string, use a for loop:

"""

def count_substring(string: str, sub_string: str) -> int:
    count: int = 0
    # starting index
    index = 0
    # ending index
    lst_index: int = len(string) - 1
    # length of index
    sub_string_length = len(sub_string)
    # loop until we get to the point of the string where checking does not make sense anymore
    while lst_index - (index + sub_string_length) > -2:
        # get current slice of string based on moving index and the size of the substring
        string_slice: str = string[index:index+sub_string_length]
        # compare them
        if  string_slice == sub_string:
            #  if they're the same increment count
            count+= 1
        # move the index to the right
        index+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)