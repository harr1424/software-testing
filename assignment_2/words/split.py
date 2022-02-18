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


test = split_words(['This', 'should', 'be', 'a', 'string.'])

print(test)