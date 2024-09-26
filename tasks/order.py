def order(sentence):
    words = {}
    result = ''
    for i in sentence.split():
        for j in range(1, len(sentence.split()) + 1):
            if str(j) in i:
                words[j] = i
                break
    for key in sorted(words):
        result += f'{words[key]} '
    return result.strip()

# https://www.codewars.com/kata/55c45be3b2079eccff00010f

