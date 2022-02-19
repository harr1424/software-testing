def split_words(sentence):
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


def count_words(sentence):
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

test_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}


test = count_words(test_dict)
print(test)




