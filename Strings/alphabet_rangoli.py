"""
Task
    You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)
    Different sizes of alphabet rangoli are shown below:

    The center of the rangoli has the first alphabet letter a, and the boundary has the  alphabet letter (in alphabetical order).

Function Description

    Complete the rangoli function in the editor below.
    rangoli has the following parameters:
        int size: the size of the rangoli

Returns

    string: a single string made up of each of the lines of the rangoli separated by a newline character (\n)

Input Format
    Only one line of input containing size, the size of the rangoli.

Constraints
    0 < size < 27
"""
import string

# intersperse an item into an inputed list
def intersperse(lst, item):
    result = [item] * (len(lst) * 2 - 1)
    result[0::2] = lst
    return result

# generate a pattern based on alphabet list and row position
def generate_pattern(alphabet: list, row: int) -> list:
    # list to hold pattern
    pattern = []
    # from 1 to 2 * line; (2 * line - 1) # of elements in first half of pattern
    for i in range(1, row + 1):
        # Append elements from backwards
        pattern.append(alphabet[-i])
    # add the elements in reverse order (relative to intial insertion)
    pattern.extend(reversed(pattern[:-1]))

    return intersperse(pattern,'-')

# generate midpoints based on width fo row and needed space of desired insert
def generate_midpoints(row_width: int, insert_width:int) -> list:
    # get center of row
    row_midpoint = row_width//2
    # get starting center point
    starting_point = row_midpoint - (insert_width // 2)
    # get end of center point 
    ending_point = (row_midpoint + (insert_width // 2)) + 1
    return [x for x in range(starting_point, ending_point)]

def generate_line(row: int, row_width: int, alphabet: list, buffer: str ) -> list:
    # list to store line
    line: list = []
    # pattern based on row
    pattern: list = generate_pattern(alphabet=alphabet, row=row+1)
    # midpoints for pattern insertion
    midpoints: list = generate_midpoints(row_width=row_width, insert_width=len(pattern))
    # line generation
    for y in range(row_width):
        if y in midpoints:
            line.append(pattern.pop(0))
        else:
            line.append(buffer)
    return line

# generate alphabet based input limit 
def generate_alphabet(limit: int) -> list:
    return list(string.ascii_lowercase[:limit])

def print_rangoli(size:int):
    # main list
    rangoli = [] 
    # alphabet list generated based on input size
    alphabet: list = generate_alphabet(size)
    # The middle pattern wil always eq the middle line
    middle_line: list = generate_pattern(alphabet=alphabet, row=size)
    # the width of the rangoli will always be eq to the middle line's width
    rangoli_width = len(middle_line)
    # for top portion of rangoli
    top_lines = []
    # from the first line to the line before the middle
    for row in range(size-1):
        # append generated line based on row, rangoli_width, alphabet, and buffer
        top_lines.append(
            generate_line(row=row, row_width=rangoli_width, alphabet=alphabet,buffer='-')
        )
    # reverse the top lines to get the bottom lines
    bottom_lines: list = reversed(top_lines)
    # add them to the main list via .extend()
    for lines in [top_lines, bottom_lines]:
        rangoli.extend(lines)
    # add the middle by inserting directly into the middle
    rangoli.insert(len(rangoli)//2, middle_line)
    # print lines in rangoli in spaced format
    for row in rangoli:
        print(''.join(map(str,row)))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)