def persistence(n):
    count = 0
    while n > 9:
        mult = 1
        for i in str(n):
            mult *= int(i)
        n = mult
        count += 1
    return count


# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec