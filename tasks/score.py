def score(dice):
    result = 0
    nums = ''.join(map(str, dice))
    for i in set(nums):
        if nums.count(i) >= 3:
            if i == '1':
                result += 1000
            else:
                result += int(i + '00')
            nums = nums.replace(i, '', 3)
            break
    for i in nums:
        if i == '1':
            result += 100
        elif i == '5':
            result += 50
    return result


# https://www.codewars.com/kata/5270d0d18625160ada0000e4
