def scramble(s1, s2):
    dct = {}
    for i in s1:
        dct[i] = dct.get(i, 0) + 1
    print(dct)
    for i in set(s2):
        if s2.count(i) > dct.get(i, 0):
            return False
    return True


# https://www.codewars.com/kata/55c04b4cc56a697bb0000048
