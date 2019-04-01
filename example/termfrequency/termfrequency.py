"""Compute term frequencies for an input file using a cookbook style"""
# !/usr/bin/env python

import sys
import re
import operator
import string
from abc import ABCMeta

#
# The classes


# pylint: disable=W1623
# pylint: disable=too-few-public-methods
from typing import Dict, List, Tuple
class TFExercise:
    """This is the abstract base class, it is meant to be extended by other classes"""

    __metaclass__ = ABCMeta

    def info(self):
        "print out the reference to the type and name of the current instance"
        return self.__class__.__name__


class DataStorageManager(TFExercise):
    """ Models the contents of the file """

    def __init__(self, path_to_file: str) -> None:
        with open(path_to_file) as f:
            self._data = f.read()
        pattern = re.compile(r"[\W_]+")
        self._data = pattern.sub(" ", self._data).lower()

    def words(self) -> List[str]:
        """ Returns the list words in storage """
        return self._data.split()

    def info(self):
        return (
            super(DataStorageManager, self).info()
            + ": My major data structure is a "
            + self._data.__class__.__name__
        )


class StopWordManager(TFExercise):
    """ Models the stop word filter """

    def __init__(self) -> None:
        with open("stopwords/stop_words.txt") as f:
            self._stop_words = f.read().split(",")
        # add single-letter words
        self._stop_words.extend(list(string.ascii_lowercase))

    def is_stop_word(self, word: str) -> bool:
        """It returns the words in the stop words"""
        return word in self._stop_words

    def info(self):
        return (
            super(StopWordManager, self).info()
            + ": My major data structure is a "
            + self._stop_words.__class__.__name__
        )


class WordFrequencyManager(TFExercise):
    """ Keeps the word frequency data """

    def __init__(self) -> None:
        self._word_freqs = {}

    def increment_count(self, word: str) -> Dict[str, int]:
        """Adds to the amount of the frequency"""
        if word in self._word_freqs:
            self._word_freqs[word] += 1
        else:
            self._word_freqs[word] = 1
        return self._word_freqs

    def sorted(self) -> List[Tuple[str, int]]:
        """Sort and return the frequency"""
        return sorted(
            self._word_freqs.items(), key=operator.itemgetter(1), reverse=True
        )

    def info(self):
        return (
            super(WordFrequencyManager, self).info()
            + ": My major data structure is a "
            + self._word_freqs.__class__.__name__
        )


class WordFrequencyController(TFExercise):
    """The object that starts the exectution of other application objects"""

    def __init__(self, path_to_file: str) -> None:
        self._storage_manager = DataStorageManager(path_to_file)
        self._stop_word_manager = StopWordManager()
        self._word_freq_manager = WordFrequencyManager()

    def run(self) -> List[Tuple[str, int]]:
        """Function that run the program"""
        for w in self._storage_manager.words():
            if not self._stop_word_manager.is_stop_word(w):
                self._word_freq_manager.increment_count(w)

        word_freqs = self._word_freq_manager.sorted()
        for (w, c) in word_freqs[0:25]:
            print(w, " - ", c)
        return word_freqs
