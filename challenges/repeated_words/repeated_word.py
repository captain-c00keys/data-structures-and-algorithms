"""Code challenge for hash tables."""


#place words into buckets
#find multiple instances of words in buckets from key
#split words into groups, remove spaces and punctuation

def Reapeated_word(input):
    """Seperate words."""
    words = input.split(' ')
    set_word = set()
    for key in words:
        if key in set_word:
            return key
