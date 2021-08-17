"""
Task:

Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. You are given scores. 
Store them in a list and find the score of the runner-up.

Input Format: 
The first line contains n The second line contains an array A[] of  n integers each separated by a space.

Constraints:
2 <= n <= 10
-100 <= A[i] <= 100

Output:

Print the runner-up score.

Explanation:

Given list is  [2,3,6,6,5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.

"""


# n = int(input())    
# arr = map(int, input().split())

# arr = list(arr)

arr = [2,2]

# DN: This will fail if n == 2
def runner_up(arr: list) -> int:
    # DN: Get Biggest # in list
    _max: int = max(arr)
    # DN: To store second biggest #
    _second_max: int = -100
    # Iterate through list
    for _ in arr:
        # Skip if the biggest #
        if _ == _max:
            continue
        # Assign if not
        if _second_max < _:
            _second_max = _

    return _second_max

print(runner_up(arr))




