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
def minion_game(string: str):
    vowels: set = {'A','E', 'I', 'O', 'U'}
    stuart_total: int = 0
    kevin_total: int = 0
    # since were searching for contingous substrings the # of substrings stirng[i] will produce is:
    # the length of the string minus it's place in the string (since it won't be using the chars before it): len(string) - index
    for index in range(len(string)):
        # for in on a set SHOULD be O(1) on average
        if string[index] in vowels:
            kevin_total += (len(s)-index)
        else:
            stuart_total += (len(s)-index)
    if kevin_total > stuart_total:
        print(f'Kevin {kevin_total}')
    elif stuart_total > kevin_total:
        print(f'Stuart {stuart_total}')
    else:
        print('Draw')
    

if __name__ == '__main__':
    s = input()
    minion_game(s)
