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

# This list is for each letter
nextLetter = []


def wordle():
    def enter_action(s):
        
        if s.lower() in FIVE_LETTER_WORDS:
            gw.set_current_row(gw.get_current_row() + 1)
        else:
            gw.show_message("invalid word entered")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Breaks word up
    for index, letter in enumerate(randomWord):
        nextLetter.append(letter)
        gw.set_square_letter(N_COLS - 5, index, letter)


# Startup code
if __name__ == "__main__":
    wordle()
