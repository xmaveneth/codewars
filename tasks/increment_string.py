def increment_string(strng: str):
    num = ''
    for i in strng[::-1]:
        if i.isdigit():
            num += i
        else:
            break
    num = num[::-1]
    strng = strng.rstrip(num)
    len_num = len(num)
    if num == '':
        num = '0'
    num = str(int(num) + 1)
    return strng + num.rjust(len_num, '0')


# https://www.codewars.com/kata/54a91a4883a7de5d7800009c
