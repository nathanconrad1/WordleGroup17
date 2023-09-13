# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

# Selects random word
randomWord = random.choice(FIVE_LETTER_WORDS)
nextLetter = []

# For previous code tries, if needed
# ([*randomWord])


def wordle():
    def enter_action(s):
        gw.show_message("You have to implement this method.")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Breaks word up
    for letter in randomWord:
        nextLetter.append(letter)

        # Adds letter to end of row
        for i in nextLetter:
            gw.set_square_letter(0, 4, i)

    print(nextLetter)


# Startup code
if __name__ == "__main__":
    wordle()
