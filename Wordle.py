# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from tkinter import *
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import (
    WordleGWindow,
    N_COLS,
    N_ROWS,
    CORRECT_COLOR,
    PRESENT_COLOR,
    MISSING_COLOR,
    WordleKey,
)

# Selects random word
randomWord = random.choice(FIVE_LETTER_WORDS)

print(randomWord)


def wordle():
    def enter_action(s):
        if s.lower() in FIVE_LETTER_WORDS:
            nextLetter = []
            chosenLetter = []
            for index, letter in enumerate(randomWord):
                nextLetter.append(letter.upper())

            for index, l in enumerate(s):
                chosenLetter.append(l.upper())
            print(chosenLetter)
            print(nextLetter)

            for index, anyLetter in enumerate(nextLetter):
                if chosenLetter[index] in nextLetter:
                    print("yellow")
                    gw.set_square_color(gw.get_current_row(), index, PRESENT_COLOR)
                if chosenLetter[index] not in nextLetter:
                    print("gray")
                    gw.set_square_color(gw.get_current_row(), index, MISSING_COLOR)
                if anyLetter == chosenLetter[index]:
                    print("green")
                    gw.set_square_color(gw.get_current_row(), index, CORRECT_COLOR)

            gw.set_current_row(gw.get_current_row() + 1)
        else:
            gw.show_message("Not in word list")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Function for Color Scheme
    # def changeColorScheme()

    # Color Scheme Button
    colorScheme = WordleKey(gw._canvas, 28, 465, 190, 50, "Change Color Scheme")

    # Share Results Button
    shareResults = WordleKey(gw._canvas, 352, 465, 122, 50, "Share Results")

    # Milestone 1:
    # Breaks word up
    # for index, letter in enumerate(randomWord):
    #     nextLetter.append(letter)
    #     gw.set_square_letter(N_COLS - 5, index, letter)


# Startup code
if __name__ == "__main__":
    wordle()
