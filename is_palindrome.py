""" is_palindrome(word) method that takes in a string word and returns the true if the word is a palindrome, false otherwise. A palindrome is a word that is spelled the same forwards and backwards."""


def is_palindrome(word):
    length = len(word)
    first = 0
    last = length - 1
    status = 1
    while(first < last):
        if(word[first] == word[last]):
            first = first+1
            last = last-1
        else:
            status = 0
            break
    return int(status)


word = input("Enter a word: ")
status = is_palindrome(word)
if(status):
    print(True)
else:
    print(False)

is_palindrome("dad")
