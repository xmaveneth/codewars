from string import ascii_lowercase, ascii_uppercase

def rot13(message):
    letters = ascii_lowercase * 2 + ascii_uppercase * 2
    result = [letters[letters.index(i) + 13] if i in letters else i for i in message]
    return ''.join(result)

# https://www.codewars.com/kata/530e15517bc88ac656000716
