def list_squared(m, n):
    result = []
    for num in range(m, n + 1):
        sum_dels = sum([i ** 2 for i in range(1, num // 2 + 1) if num % i == 0] + [num ** 2])
        if sum_dels ** 0.5 == int(sum_dels ** 0.5):
            result.append([num, sum_dels])
    return result

# https://www.codewars.com/kata/55aa075506463dac6600010d
