def array_diff(a: list, b: list):
    for el in b:
        while el in a:
            a.remove(el)
    return a

# https://www.codewars.com/kata/523f5d21c841566fde000009