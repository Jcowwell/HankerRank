"""
Task:

Given an integer, n, perform the following conditional actions:
If  n is odd, print Weird
If  n is even and in the inclusive range of 2 to 5, print Not Weird
If  n is even and in the inclusive range of 6 to 20, print Weird
If  n is even and greater than 20, print Not Weird

Input Format: 
A single line containing a positive integer, n.

Constraints:
1 < n < 100

Output:

Print Weird if the number is weird. Otherwise, print Not Weird.

"""

weird: str = "Weird"
not_weird: str = 'Not Weird'


def _is_odd(n: int) -> bool:
    if (n % 2 != 0):
        return True
    return False

def is_weird(n: int) -> str:
    if _is_odd(n=n):
        return weird
    if n in range(2,6):
        return not_weird
    if n in range(6,21):
        return weird
    else:
        return not_weird
