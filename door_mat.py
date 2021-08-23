"""
Task
    Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
        Mat size must be NxM. (N is an odd natural number, and M is 3 times N.)
        The design should have 'WELCOME' written in the center.
        The design pattern should only use |, . and - characters.

Input Format
    A single line containing the space separated values of N and M.

Constraints
    5 < N < 101
    15 < M < 303

Output Format
    Output the design pattern.
"""

# gets midpoints of a row based on how long of an input. used to insert an input in trhe middle. 
def _midpoints(input: int, insert_size:int) -> list:
    input_midpoint = input//2
    left_starting_point = input_midpoint - (insert_size // 2)
    right_ending_point = (input_midpoint + (insert_size // 2)) + 1
    return [x for x in range(left_starting_point, right_ending_point)]

# creates row pattern of a row based on an = (2n - 1) arthimetic sequence
def _row_pattern(pattern: list, index: int) -> list:
    # used to adjust array to be based on postioning
    index+= 1
    #  creates (2n -1) amount of a pattern based on input
    return pattern * (2 * index - 1)

# creates outer pattern sequence for an input row and column
def _outer_patttern(row: int, column: int, pattern: list, border: str) -> list:
    # list to store row patterns
    row_pattern: list = []
    # pattern based on which row were on 
    patterns: list = _row_pattern(pattern=pattern, index=row)
    # row center points, used for inserting pattern in center of row
    row_center_points: list = _midpoints(input=column, insert_size=len(patterns))
    for y in range(column): # Columns
        # if in the center of row 
        if (y in row_center_points):
            # append pattern
            row_pattern.append(patterns.pop(0))
        else:
            # append pattern 
            row_pattern.append(border)
    return row_pattern

# creates middle pattern sequence for input column, middle row is calcualted beforehand
def _mid_pattern(column: int, pattern: list, border: str) -> list:
     # list to store row pattern
    row_pattern: list = []
    # row center points, used for inserting pattern in center of row
    center_points = _midpoints(input=column,insert_size=len(pattern))
    for y in range(column):
        # if in the center of the row
        if (y in center_points):
            # append pattern
            row_pattern.append(pattern.pop(0))
        else:
            # append border
            row_pattern.append(border)
    return row_pattern

def generate_door_mat(row: int, column: int, center_pattern: list, pattern: list, border: str):
    # main matrix
    matrix = []
    # segmented parts of matrix
    top: list= [] ; center: list = [] ; bottom: list = []
    # midpoint of row
    row_midpoint = row//2
    # Top + Middle
    # iterate until we get to centter of desired matrix input
    for row_index in range(row_midpoint + 1): # Rows
        # Top - Top Part of Pattern
        if row_index < row_midpoint:
            top.append(
                _outer_patttern(row=row_index, column=column, pattern=pattern, border=border)
            )
        # MIDDLE - Middle Part of Pattern
        if row_index == row_midpoint:
            center.append(
                    _mid_pattern(column=column, pattern=center_pattern, border=border)
                )
    # BOTTOM - Bottom Part of Pattern (Top Reversed)
    for row_index in range((row_midpoint)):
        if row_index < row_midpoint:
            bottom.append(
                _outer_patttern(row=row_index, column=column, pattern=pattern, border=border)
            )
    # reverse bottom part to mirror top
    bottom.reverse()
    # merge parts into single matrix
    for part in [top, center, bottom]:
        matrix.extend(part)
    return matrix
    

center_pattern = ['W','E','L','C','O','M','E']
pattern = ['.','|','.']
border = '-'
row, column = input().split()
matrix = generate_door_mat(row=int(row), column=int(column), center_pattern=center_pattern, pattern=pattern, border = border )
for row in matrix:
    print(''.join(map(str,row)))




