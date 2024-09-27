def rgb(r, g, b):
    result = []
    for i in [r, g, b]:
        if 0 <= i <= 255:
            result.append(hex(i)[2:].upper().rjust(2, '0'))
        elif i < 0:
            result.append('00')
        else:
            result.append('FF')
    return ''.join(result)


# https://www.codewars.com/kata/513e08acc600c94f01000001
