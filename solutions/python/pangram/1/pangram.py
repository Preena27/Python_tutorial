import string
def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    sentence_letters = set(sentence.lower())
    return alphabet <= sentence_letters

