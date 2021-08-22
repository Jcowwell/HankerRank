"""
Task
You are given a string S.
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits,

Input Format
    A single line containing a string S.

Constraints
    0 < len(S) < 1000
Output Format
    In the first line, print True if S has any alphanumeric characters. Otherwise, print False. 
    In the second line, print True if S has any alphabetical characters. Otherwise, print False. 
    In the third line, print True if S has any digits. Otherwise, print False. 
    In the fourth line, print True if S has any lowercase characters. Otherwise, print False. 
    In the fifth line, print True if S has any uppercase characters. Otherwise, print False.
"""




def validator(s:str) -> bool:
    # since any() stops the it's iteration upon the first hit, we can use it along witht the built-in is_x methods to check is a char flags as a alphanumeric, alphabet, digit , lowercase or uppercase
    return [flag for flag in (any(method(c) for c in s) for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper])]

if __name__ == '__main__':
    s: str = input()
    flags = validator(s=s)
    for flag in flags:
        print(flag)

    
    
