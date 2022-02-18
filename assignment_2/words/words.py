from typing import List

import pytest

"""
John Harrington
Software Reliability and Testing, Spring, 2022
Assignment Two 

In this assignment submission, doctests are preferentially used to highlight intended use cases of functions 
and so the tests written as doctests are intended to succeed. Tests have also been written which are intended 
to fail, and these are included as unit tests at the end of the file. Unit tests have been used preferentially 
for tests that should fail because these tests involve asserting unhandled exceptions.

KNOWN ISSUES: 
join_words() is defined to accept a list of strings. If this function is passed a single string, 
instead of raising a TypeError, it will return the string with a single space added between each character.
"""


def split_words(sentence: str) -> List[str]:
    """
    Split a string into a list of words. A word boundary is defined to be any
    number of space or tab characters.
    >>> split_words("Hello World")
    ['Hello', 'World']
    >>> split_words("Tab\tTest")
    ['Tab', 'Test']
    >>> split_words("Multiple                   Spaces")
    ['Multiple', 'Spaces']
    >>> split_words("Multiple\t\t\t\t\t\tTabs")
    ['Multiple', 'Tabs']
    >>> split_words("Now we are testing\ta combination \t of tabs\tand \tspaces.")
    ['Now', 'we', 'are', 'testing', 'a', 'combination', 'of', 'tabs', 'and', 'spaces.']
    >>> split_words("")
    []
    >>> split_words("\t")
    []
    """
    words = []
    next_word = ""

    for character in sentence:
        if character == " ":
            if next_word != "":
                words.append(next_word)
                next_word = ""
        else:
            next_word = next_word + character

    if next_word != "":
        words.append(next_word)

    return words


def join_words(words: List[str]) -> str:
    """
    Take a list of words and return it as a sentence, with adjacent words
    separated by a single space character.
    >>> join_words(['Hello', 'World'])
    'Hello World'
    >>> join_words(['Hello', 'world', 'how', 'are', 'you', 'today?'])
    'Hello world how are you today?'
    >>> join_words([])
    ''
    >>> join_words(['Empty', '', 'strings', '', 'yield', '', 'spaces.'])
    'Empty  strings  yield  spaces.'
    """
    sentence = ""

    for word in words:
        if sentence != "":
            sentence = sentence + " "
        sentence = sentence + word

    return sentence


def count_words(sentence: str) -> int:
    """
    Count the number of words in the sentence. A word boundary is defined to be
    any number of space or tab characters.
    >>> count_words("Hello world!")
    2
    >>> count_words('')
    0
    >>> count_words("\t")
    0
    >>> count_words("Multiples spaces          should be treated   as one space.")
    8
    >>> count_words("Testing \ttabs\t and\t \t spaces")
    4
    """
    return len(split_words(sentence))


# Use unit testing to write tests that should fail

test_dict = {
    "a" : 1,
    "b" : 2,
    "c" : 3,
    "d" : 4
}

def test_split_words_illegal_arg_type():
    with pytest.raises(TypeError):
        split_words(108)


def test_split_words_illegal_num_args():
    with pytest.raises(TypeError):
        split_words("Hello", "World")


def test_join_words_illegal_arg_type_string():
    with pytest.raises(TypeError):
        join_words("This, should, be, a, list")
        """
        This test does not perform as expected, and indicates an error with the join_words
        function. If a string is passed to this function, instead of raising a TypeError, 
        join_words will return the string with an added space in between each character of the string.
        """

def test_join_words_illegal_arg_type_int():
    with pytest.raises(TypeError):
        join_words(108)


def test_join_words_illegal_arg_type_boolean():
    with pytest.raises(TypeError):
        join_words(False)


def test_join_words_illegal_arg_type_dict():
    with pytest.raises(TypeError):
        join_words(test_dict)
        """
        This test does not perform as expected, and indicates an error with the join_words
        function. If a dictionary is passed to this function, instead of raising a TypeError, 
        join_words will return the dictionary keys.
        """

def test_join_Words_illegal_arg_type_tuple():
    with pytest.raises(TypeError):
        join_words(("This", "should", "be", "a", "list."))
        """
        This test does not perform as expected, and indicates an error with the join_words
        function. If a tuple is passed to this function, instead of raising a TypeError, 
        join_words will return the tuple with an added space in between each item of the tuple.
        """

def test_join_words_illegal_num_args():
    with pytest.raises(TypeError):
        join_words(['list', 'one'], ['list', 'two'])




