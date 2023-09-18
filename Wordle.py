# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR

# Selects random word
randomWord = random.choice(FIVE_LETTER_WORDS)

# Milestone 1:
# This list is for each letter
nextLetter = []


def wordle():
    def enter_action(s):
        if s.lower() in FIVE_LETTER_WORDS:
            chosenLetter = []
            for index, letter in enumerate(randomWord):
                nextLetter.append(letter)
                # gw.set_square_letter(N_COLS - 5, index, letter)

            for index, l in enumerate(s):
                chosenLetter.append(l)
                # gw.set_square_letter(N_COLS - 5, index, l)
            gw.set_current_row(gw.get_current_row() + 1)

            x = 0

            for anyLetter in nextLetter:
                if anyLetter == chosenLetter[x]:
                    gw.set_square_color(gw.get_current_row(), x, CORRECT_COLOR)

        else:
            gw.show_message("Not in word list")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Milestone 1:
    # Breaks word up
    # for index, letter in enumerate(randomWord):
    # nextLetter.append(letter)
    # gw.set_square_letter(N_COLS - 5, index, letter)


# Startup code
if __name__ == "__main__":
    wordle()
