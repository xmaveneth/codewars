def move_zeros(lst: list):
    count = 0
    while 0 in lst:
        lst.remove(0)
        count += 1
    return lst + [0] * count


# https://www.codewars.com/kata/52597aa56021e91c93000cb0
