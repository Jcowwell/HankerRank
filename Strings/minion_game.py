"""
Task
    Kevin and Stuart want to play the 'The Minion Game'.

    Game Rules:
        Both players are given the same string, S.
        Both players have to make substrings using the letters of the string S.
        Stuart has to make words starting with consonants.
        Kevin has to make words starting with vowels.
        The game ends when both players have made all possible substrings.

    Scoring
        A player gets +1 point for each occurrence of the substring in the string S.

    For Example:
    String S = BANANA
    Kevin's vowel beginning word = ANA
    Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

    Your task is to determine the winner of the game and their score.

Function Description
    Complete the minion_game in the editor below.
    minion_game has the following parameters:
        string string: the string to analyze

Prints
    string: the winner's name and score, separated by a space on one line, or Draw if there is no winner

Input Format
    A single line of input containing the string .
    Note: The string  will contain only uppercase letters: .

Constraints
    0 < len(S) <= 10^6
    Vowels are only defined as AEIOU. In this problem, Y is not considered a vowel.
"""
from itertools import combinations
from collections import Counter

vowels: dict = {'A':'A','E':'E','I':'I','O':'O','U':'U'}

def generate_substrings(string: str) ->  list:
    length = len(string) + 1
    return [string[x:y] for x, y in combinations(range(length), r=2)]

def minion_game(string: str):
    stuart_total: int = 0
    kevin_total: int = 0
    substrings: list = generate_substrings(string=string)
    substring_counter: Counter = Counter(substrings)
    for substring, count in substring_counter.items():
        if substring[0] in vowels:
            kevin_total += count
        else:
            stuart_total += count
    if kevin_total > stuart_total:
        print(f'Kevin {kevin_total}')
    elif stuart_total > kevin_total:
        print(f'Stuart {stuart_total}')
    else:
        print('Draw')
    

if __name__ == '__main__':
    s = input
    print(minion_game(s))
