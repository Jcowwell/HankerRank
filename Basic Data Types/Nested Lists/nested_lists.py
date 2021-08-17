"""
Task:
Given the names and grades for each student in a class of  N students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example:
records = [["chi",20.0],["beta"],50.0],["alpha",50.0]]

The ordered list of scores is [20.0, 50.0], so the second lowest score is 50.0. 
There are two students with that score: ["beta","alpha"]. Ordered alphabetically, the names are printed as:
alpha
beta

Input Format: 
The first line contains an integer, N, the number of students. 
The 2N subsequent lines describe each student over 2 lines. 
- The first line contains a student's name. 
- The second line contains their grade.

Constraints:
2 <= n <= 5

Output:

Print the name(s) of any student(s) having the second lowest grade in. 
If there are multiple students, order their names alphabetically and print each one on a new line.

"""

num_of_students = int(input())
names: list = []
grades: list = []
records: list = []

for _ in range(num_of_students):
    names.append(input())
    grades.append(float(input()))
    
#  DN: Yes this is cheating, no I don't care. Screw duplicates. 
def second_minima(set: set) -> set:
    set.remove(min(set))
    return min(set)

def second_worst(names: list, grades: list) -> list:
    # DN: Loop through lists based on num_of_students
    for _ in range(num_of_students):
        records.append([names[_], grades[_]])

    # DN: List to store second to last worst grade students
    second_to_last: list = []

    # DN: Iterate through records to see who might have same grades
    for record in records:
        if record[1] == second_minima(set(grades)):
            second_to_last.append(record[0])

    second_to_last.sort()
    return second_to_last

for _ in second_worst(names=names,grades=grades):
    print(_)




