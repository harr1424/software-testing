from typing import List

import pytest

"""
John Harrington
Software Reliability and Testing, Spring, 2022
Assignment Two 

In this assignment submission, doctests are preferentially used to highlight intended use cases of functions 
and so the tests written as doctests are intended to succeed. Tests have also been written which are intended 
to fail, and these are included as unit tests at the end of the file. Unit tests have been used preferentially 
for tests that should fail because these tests involve unhandled exceptions.

KNOWN ISSUES: 
join_words() is defined to accept a list of strings. If this function is passed a single string, tuple, or dictionary
instead of raising a TypeError, it will return the string, sequence, or keys with a single space added between 
each character in the sequence or key list. An exhaustive set of type that produce this behavior has not been tested, 
but it is certain that this function should perform a type check to ensure only a list is passed as described 
in the function's documentation. 

Similarly, split_words() behaves unexpectedly when sequence or mapping types are passed as arguments, 
and should also be updated to raise a TypeError when any type besides a string is passed as an argument. 

Finally, count_words() also behaves unexpectedly when sequence or mapping types are passed as arguments, 
and should also be updated to raise a TypeError when any type besides a string is passed as an argument. 
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
    'Empty  strings  yield  spaces.'`
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


# Dictionary to be used in unit testing
test_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}


def test_split_words_illegal_arg_type_int():
    with pytest.raises(TypeError):
        split_words(108)


def test_split_words_illegal_arg_type_list_of_strings():
    with pytest.raises(TypeError):
        split_words(['This', 'should', 'be', 'a', 'string.'])
        """
        This test does not perform as expected, and indicates an error with the split_words function. 
        When a list is passed to this function, instead of raising a TypeError, the function will 
        join list items (in this case strings) without spaces and return a single item.
        """


def test_split_words_illegal_arg_type_list_of_ints():
    with pytest.raises(TypeError):
        split_words([4, 8, 15, 16, 23, 42])


def test_split_words_illegal_arg_type_boolean():
    with pytest.raises(TypeError):
        split_words(False)


def test_split_words_illegal_arg_type_dict():
    with pytest.raises(TypeError):
        split_words(test_dict)
        """
        This test does not perform as expected, and indicates an error with the split_words function. 
        When a dict is passed to this function, instead of raising a TypeError, the function will 
        return the dictionary keys.
        """


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


def test_join_words_illegal_arg_type_tuple():
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


def test_count_words_illegal_arg_type_int():
    with pytest.raises(TypeError):
        count_words(108)


def test_count_words_illegal_arg_type_list_of_words():
    with pytest.raises(TypeError):
        count_words(['This', 'should', 'be', 'a', 'string.'])
        """
        This test does not perform as expected, and indicates an error with the count_words
        function. If a single list of strings is passed as an argument, count_words() will return 
        a count of 1. 
        """


def test_count_words_illegal_arg_type_list_of_ints():
    with pytest.raises(TypeError):
        count_words([4, 8, 6])


def test_count_words_illegal_arg_type_boolean():
    with pytest.raises(TypeError):
        count_words(False)


def test_count_words_illegal_arg_type_dict():
    with pytest.raises(TypeError):
        count_words(test_dict)
        """
        This test does not perform as expected, and indicates an error with the count_words
        function. If a dictionary is passed as an argument, count_words() will return a count of 1.
        """


def test_count_words_illegal_num_args():
    with pytest.raises(TypeError):
        count_words("Sentence one.", "Sentence two.")










