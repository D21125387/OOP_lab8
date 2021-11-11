from random import shuffle
from WordGame import WordGames


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
