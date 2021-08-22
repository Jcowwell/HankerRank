"""
Task
    You are given the firstname and lastname of a person on two different lines. 
    Your task is to read them and print the following:
        Hello firstname lastname! You just delved into python.

Function Description
    Complete the print_full_name function in the editor below.
    print_full_name has the following parameters:
        string first: the first name
        string last: the last name
    string: 'Hello firstname lastname ! You just delved into python' where firstname and lastname are replaced with first and last.

Input Format
    The first line contains the first name, and the second line contains the last name. Constraints
    The length of the first and last name ≤ 10.

Output Format
    Print the output as mentioned above.
"""

def print_full_name(first: str, last: str):
    print(
        f'Hello {first} {last}! You just delved into python.'
    )

if __name__ == '__main__':
    first_name: str = input()
    last_name: str = input()
    print_full_name(first_name, last_name)