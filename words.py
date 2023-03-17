def print_upper_words3(words):
    """turns list of words into uppercase versions of the word"""
    for word in words:
        print(word.upper())


def print_upper_words2(words):
    """turns list of words into uppercase versions of the word only if the word starts with e"""

    for word in words:
        if word[0] == "e":
            print(word.upper())


def print_upper_words_with_letters3(words, letters):
    """turns list of words into uppercase versions of the word only if the word starts with the passed in letter"""

    for word in words:
        for letter in letters:
            if word.startswith(letter):
                print(word.upper())
