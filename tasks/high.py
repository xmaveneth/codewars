from string import ascii_lowercase

def high(x):
    words = x.split()
    result = ''
    for el in words:
        if count_score(el) > count_score(result):
            result = el
    return result

def count_score(word):
    return sum([ascii_lowercase.find(i) + 1 for i in word])

# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272
