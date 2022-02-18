from typing import List

"""
John Harrington
Software Reliability and Testing, Spring, 2022
Assignment Two 

In this assignment submission, doctests are preferentially used to highlight intended use cases of functions 
and so the tests written as doctests are intended to succeed. Tests have also been written which are intended 
to fail, and these are included as unit tests at the end of the file. Unit tests have been used preferentially 
for tests that should fail because these tests involve asserting unhandled exceptions and errors and so including 
these tests as unit tests instead of doctests makes this submission significantly more readable
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
    >>> count_words("Multipls spaces          should be treated   as one space.")
    8
    >>> count_words("Testing \ttabs\t and\t \t spaces")
    4
    """
    return len(split_words(sentence))



# TODO use unit tsting to write tests that should fails
# Explore asserting unhandled exceptions
# Also test extremely large strings using project Gutenberg