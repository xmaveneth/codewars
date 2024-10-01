def is_simple(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_factors(n):
    dct = {}
    dlt = 2
    while n != 1:
        if is_simple(n):
            dct[n] = dct.get(n, 0) + 1
            break
        elif is_simple(dlt) and n / dlt == n // dlt:
            dct[dlt] = dct.get(dlt, 0) + 1
            n //= dlt
        else:
            dlt += 1
    result = ''
    for i in dct.keys():
        if dct[i] > 1:
            result += f'({i}**{dct[i]})'
        else:
            result += f'({i})'
    return result


# https://www.codewars.com/kata/54d512e62a5e54c96200019e
