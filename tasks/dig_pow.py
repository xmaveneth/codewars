def dig_pow(n, p):
    num = 0
    for i in range(len(str(n))):
        num += int(str(n)[i]) ** (p + i)
    return int(num / n) if num / n == int(num / n) else -1


# https://www.codewars.com/kata/5552101f47fc5178b1000050
