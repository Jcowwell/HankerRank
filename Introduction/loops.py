"""
Task:
The provided code stub reads and integer, n , from STDIN. For all non-negative integers i < n, print i^2 .

Input Format: 
The first line contains the first integer, a. 
The second line contains the second integer, b.

Constraints:
1 <= n <= 20

"""

n = int(input())

# DN: - "Quadratic comes from "quad" meaning square; when you raise something to the second power, you square it"
def quad(i:int) -> int:
    return i * i

def print_quad_until(n:int):
    for _ in range(0,n):
        print(quad(_))
    
print_quad_until(n)