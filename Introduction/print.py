"""
Task:
The included code stub will read an integer, n , from STDIN.
Without using any string methods, try to print the following:
123...n
Note that "..." represents the consecutive values in between.

Example: 
n = 5

Print the string 12345.

Input Format: 
The first line contains an integer n.

Constraints:
1 <= year <= 150

"""
n = int(input())

# DN: ( (n+1) / 2) in bionomial coefficient form
def triangle_number(n: int) -> int:
    for _ in range(1,n + 1):
        print(_, end="")

triangle_number(n)