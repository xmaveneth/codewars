def digital_root(n):
    while n > 9:
        n = sum([int(i) for i in str(n)])
    return n

# https://www.codewars.com/kata/541c8630095125aba6000c00