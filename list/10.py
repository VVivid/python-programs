""" Write a Python program to find the list of words
 that are longer than n from a given list of words."""


def find_length(n, input):

    txt = input.split(" ")
    word_len = [item for item in txt if len(item) > n]
    return word_len


print(find_length(3, "The quick brown fox jumps over the lazy dog"))
