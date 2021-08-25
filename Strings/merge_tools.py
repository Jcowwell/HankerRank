"""
Task
    Consider the following:
        A string, s, of length n where s=c0c1...cn-1.
        An integer, k, where k is a factor of n.
    We can split s into n/k subsegments where each subsegment, ti , consists of a contiguous block of k
    characters in s. Then, use each to create string such that:
        The characters in ui are a subsequence of the characters in ti.
        Any repeat occurrence of a character is removed from the string such that each character in ui
    occurs exactly once. In other words, if the character at some index j in ti occurs at a previous index
    < j in ti, then do not include the character in string ui.
    Given s and k, print n/k lines where each line i denotes string ui.

Input Format
    The first line contains a single string denoting .
    The second line contains an integer, , denoting the length of each subsegment.

Constraints
    1 <= n <= 10^4, where n = 8
    1 <= k <= n
    It is guaranteed that is a multiple of k.

Output Format
    Print n/k lines where each line i contains string ui .
"""
def generate_contigous_substrings(string: str, length: int, k: int) -> list:
    substrings = []
    for index in range(0, length, k):
         substrings.append(string[index:index+k])
    return substrings

def uniquify(string: str) -> str:
    return ''.join(dict.fromkeys(string))

def merge_the_tools(string: str, k: int):
    n: int = len(string)
    substrings = generate_contigous_substrings(string=string, length=n, k=k)
    for substring in substrings:
        print(uniquify(substring))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)