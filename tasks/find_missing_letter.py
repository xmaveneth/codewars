from string import ascii_lowercase

def find_missing_letter(chars):
    letters = ascii_lowercase
    if chars[0].isupper():
        letters = letters.upper()

    idx = letters.find(chars[0])
    letters = letters[idx:]

    for i in range(len(chars)):
        if chars[i] != letters[i]:
            return letters[i]

# https://www.codewars.com/kata/5839edaa6754d6fec10000a2
