def zero(data=''):
    if data:
        return eval('0' + data)
    return '0'

def one(data=''):
    if data:
        return eval('1' + data)
    return '1'

def two(data=''):
    if data:
        return eval('2' + data)
    return '2'

def three(data=''):
    if data:
        return eval('3' + data)
    return '3'

def four(data=''):
    if data:
        return eval('4' + data)
    return '4'

def five(data=''):
    if data:
        return eval('5' + data)
    return '5'

def six(data=''):
    if data:
        return eval('6' + data)
    return '6'

def seven(data=''):
    if data:
        return eval('7' + data)
    return '7'

def eight(data=''):
    if data:
        return eval('8' + data)
    return '8'

def nine(data=''):
    if data:
        return eval('9' + data)
    return '9'

def plus(func):
    return '+' + func


def minus(func):
    return '-' + func

def times(func):
    return '*' + func

def divided_by(func):
    return '//' + func

print(zero(plus(nine())))
print(six(divided_by(two())))