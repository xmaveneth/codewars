def spin_words(sentence):
    return ' '.join([i[::-1] if len(i) >= 5 else i for i in sentence.split()])

# https://www.codewars.com/kata/5264d2b162488dc400000001