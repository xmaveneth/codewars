def narcissistic(value):
    nums = [int(i) ** len(str(value)) for i in str(value)]
    return value == sum(nums)

# https://www.codewars.com/kata/5287e858c6b5a9678200083c
