def find_it(seq):
    nums = set(seq)
    for el in seq:
        if seq.count(el) % 2:
            return el


# https://www.codewars.com/kata/54da5a58ea159efa38000836