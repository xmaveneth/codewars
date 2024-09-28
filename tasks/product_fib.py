def fibonacci(num):
    a1, a2 = 0, 1
    for i in range(num):
        a1, a2 = a2, a1 + a2
    return a1

def product_fib(_prod):
    mult = -1
    num = 0
    while mult < _prod:
        mult = fibonacci(num) * fibonacci(num + 1)
        num += 1
    return [fibonacci(num - 1), fibonacci(num), mult == _prod]


# https://www.codewars.com/kata/5541f58a944b85ce6d00006a
