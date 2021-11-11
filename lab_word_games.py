# course: Object-oriented programming, year 2, semester 1
# academic year: 2021-20
# author: B. Schoen-Phelan
# date: 11-11-2021
# purpose: Lab wk8 - Word Games

# base class
from random import shuffle


class WordGames:
    """
    Class to represent the word game's base class.
    Methods and attributes that every type of word
    game should have are defined here.
    ...
    Attributes:
    -----------
        _my_words : str
        Read from user input and identifies the word
        or sentence that a user has inputted.

    Methods:
    --------
        the_words:
            Property getter method that returns
            the value of the user inputted word
            or sentence

        word_play:
            Contains logic for playing the game.
            Child classes should override this
            method in order to implement their own
            game logic.
    """

    def __init__(self):
        """
        Constructs the necessary attributes for the
        WordGame object.

        Parameters: None.
        -----------

        Instance variables:
        -------------------
            _my_words : str
                Variable that holds the user inputted word or
                sentence. Set to enforced encapsulation via
                name mangling.
        """
        self._my_words = input("Please enter a word or sentence: ")

    @property
    def the_words(self):
        """
        Property method to return the value of the user
        inputted word or sentence.

        Parameters: None.
        -----------

        Returns:
        ________
            _my_words : str
                The value of the word or sentence that has
                been inputted by a user.
        """
        return self._my_words

    def word_play(self):
        """
        Plays the game. The base class version of playing
        the game simply prints the value that has been
        inputted.

        Parameters: None.
        -----------

        Returns: None.
        --------
        """
        print("User input was: " + self.the_words)


class WordDuplication(WordGames):  # you implement this and provide docstrings
    """
    Plays the game. The extended class version duplicates
    the list and print as String

    Override word_play()

    Parameters: None.
    -----------

    Returns: None.
    --------
    """

    def word_play(self):
        words = self.the_words.split(" ")
        words *= 2
        sentence = ' '.join(words)
        print(sentence)


class WordScramble(WordGames):  # you implement this and provide docstrings
    """
    Plays the game. The extended class version scramble/shuffle
    the list and print as String

    Override word_play()

    Parameters: None.
    -----------

    Returns: None.
    --------
    """

    def word_play(self):
        words = self.the_words.split(" ")
        sentence = ""
        for i in words:
            word = list(i)
            shuffle(word)
            word = ' '.join(word)
            sentence += word
        print(sentence)


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
