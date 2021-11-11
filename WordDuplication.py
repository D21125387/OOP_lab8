from WordGame import WordGames


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