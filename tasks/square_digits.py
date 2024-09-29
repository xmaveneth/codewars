def square_digits(num):
    data = [str(int(i) ** 2) for i in str(num)]
    return int(''.join(data))