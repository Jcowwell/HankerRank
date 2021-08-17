"""
Task:
The provided code stub reads two integers, a and b, from STDIN.
Add logic to print two lines. The first line should contain the result of integer division,  a//b . The second line should contain the result of float division,  a/b .
No rounding or formatting is necessary.

Input Format: 
The first line contains the first integer, a. 
The second line contains the second integer, b.
"""

a = int(input())
b = int(input())

def _int_division(a:int, b:int) -> int:
    try:
        return a // b
    except ZeroDivisionError:
        return 0

def _float_division(a:int, b:int) -> float:
    try:   
        return a / b
    except ZeroDivisionError:
        return 0.0

def print_division(a:int, b:int):
    int_division_ = _int_division(a=a,b=b)
    float_division_ = _float_division(a=a,b=b)

    print(
        (f"{int_division_}\n" 
        f"{float_division_}"
        )
    )

print_division(a=a,b=b)