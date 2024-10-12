def sort_array(source_array):
    evens = {}
    result = []
    for i, el in enumerate(source_array):
        if el % 2:
            result.append(el)
        else:
            evens[i] = el

    result.sort()

    for key, value in evens.items():
        result.insert(key, value)

    return result

# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d
