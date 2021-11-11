# course: Object-oriented programming, year 2, semester 1
# academic year: 2021-20
# author: B. Schoen-Phelan
# date: 11-11-2021
# purpose: Lab wk8 - Word Games

# base class
from WordGame import WordGames
from WordDuplication import WordDuplication
from WordScramble import WordScramble


# prints the docstrings info
# if this class was a python module
print(WordGames.__doc__)
print(WordDuplication.__doc__)
print(WordScramble.__doc__)

# Create an instances of the classes here:
# wg = WordGames()
# wg.word_play()

ws = WordDuplication()
ws.word_play()
