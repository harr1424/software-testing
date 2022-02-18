def join_words(words):
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


test_dict = {
    "a" : 1,
    "b" : 2,
    "c" : 3,
    "d" : 4
}

test_var = join_words(("This", "should", "be", "a", "list."))
print(test_var)