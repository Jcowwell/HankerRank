"""
Task:
The provided code stub reads two integers from STDIN a and b. Add code to print three lines where:
1. The first line contains the sum of the two numbers.
2. The second line contains the difference of the two numbers (first - second).
3. The third line contains the product of the two numbers.

Input Format: 
The first line contains the first integer, a. 
The second line contains the second integer, b.

Constraints:
1 <= a < 10^10
1 <= b < 10^10
"""

a = int(input())
b = int(input())

def _sum(a:int, b:int) -> int:
    return a + b

def _diff(a:int, b:int) -> int:
    return a - b

def _product(a:int, b:int) -> int:
    return a * b

def print_arthmetric(a:int, b:int):
    sum_ = _sum(a=a,b=b)
    diff_ = _diff(a=a,b=b)
    product_ = _product(a=a,b=b)

    print(
        (f"{sum_}\n" 
        f"{diff_}\n" 
        f"{product_}"
        )
    )

print_arthmetric(a=a,b=b)

