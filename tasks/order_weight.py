def order_weight(strng: str):
    data = strng.strip().split()
    data.sort(key=lambda x: (sum([int(i) for i in x]), x))
    return ' '.join(data)


# https://www.codewars.com/kata/55c6126177c9441a570000cc
