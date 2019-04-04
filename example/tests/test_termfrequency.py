"""Test cases for the object-oriented implementation"""

import subprocess
import pytest

from termfrequency import termfrequency


def test_read_file_populates_data_0():
    """ Checks that the reading of the small text file works """
    storage_manager = termfrequency.DataStorageManager("inputs/input.txt")
    word_list = storage_manager.words()
    assert word_list is not None
    assert len(word_list) == 12


def test_DataStorageManager_return_info():
    """ Checks that the info() works """
    storage_manager = termfrequency.DataStorageManager("inputs/input.txt")
    word = storage_manager.info()
    assert word == "DataStorageManager: My major data structure is a str"


def test_StopWordManager_stop_word():
    """ Checks that the stop_word works by passing in a list of stop words"""
    word = ["able", "about", "across"]
    stopword_manager = termfrequency.StopWordManager()
    word_test = stopword_manager.is_stop_word(word)
    assert word_test is False


def test_StopWordManager_info():
    """ Checks that the info() works """
    stopword_manager = termfrequency.StopWordManager()
    return_msg = stopword_manager.info()
    assert return_msg == "StopWordManager: My major data structure is a list"


def test_WordFrequencyManager_frequent_count():
    """ Checks that the count() works by putting in uncounted list"""
    words = ["tiger", "frequency", "frequency", "frequency"]
    frequency_manager = termfrequency.WordFrequencyManager()
    for w in words:
        freq_word = frequency_manager.increment_count(w)
    assert freq_word == {"tiger": 1, "frequency": 3}


def test_WordFrequencyManager_frequent_sort():
    """ Checks that the sorted() works by putting in unsorted list"""
    words = ["tiger", "frequency", "frequency", "frequency"]
    frequency_manager = termfrequency.WordFrequencyManager()
    for w in words:
        frequency_manager.increment_count(w)
    sorted_word = frequency_manager.sorted()
    assert sorted_word == [("frequency", 3), ("tiger", 1)]


def test_WordFrequencyManager_info():
    """ Checks that the info() works """
    frequency_manager = termfrequency.WordFrequencyManager()
    return_msg = frequency_manager.info()
    assert return_msg == "WordFrequencyManager: My major data structure is a dict"


def test_WordFrequencyController_run():
    """ Checks that the run() works by asserting the output equals to the expected"""
    frequency_controller = termfrequency.WordFrequencyController(
        "inputs/input.txt"
    )
    word_freqs = frequency_controller.run()
    assert word_freqs == [
        ("live", 2),
        ("mostly", 2),
        ("white", 1),
        ("tigers", 1),
        ("india", 1),
        ("wild", 1),
        ("lions", 1),
        ("africa", 1),
    ]


def test_main():
    """Capture program's output to check if it's right"""
    result = subprocess.run(
        ["python3", "termfrequency/termfrequency.py", "inputs/input.txt"],
        stdout=subprocess.PIPE,
    )
    output = result.stdout.decode("utf-8")
    expected = (
        "live  -  2\nmostly  -  2\nwhite  -  1\n"
        "tigers  -  1\nindia  -  1\nwild  -  1\n"
        "lions  -  1\nafrica  -  1\n"
    )
    assert output == expected


@pytest.mark.parametrize(
    "input_list,expected_count",
    [(["world", "world", "world"], 3), (["frequency", "frequency"], 2), ([""], 1)],
)
def test_WordFrequencyManager_frequent_count_parametrize(input_list, expected_count):
    """ Checks that the count() works adopting parametrize testing"""
    frequency_manager = termfrequency.WordFrequencyManager()
    for w in input_list:
        freq_word = frequency_manager.increment_count(w)
    for w in freq_word:
        assert freq_word[w] == expected_count
