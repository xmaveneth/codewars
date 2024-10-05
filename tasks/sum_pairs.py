def sum_pairs(ints, s):
    seen = set()
    for num in ints:
        complement = s - num
        if complement in seen:
            return [complement, num]
        seen.add(num)
    return None


# https://www.codewars.com/kata/54d81488b981293527000c8f
