def duplicate_encode(word):
    word = word.lower()
    return ''.join(['(' if word.count(i) == 1 else ')' for i in word])


# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c
