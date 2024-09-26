def narcissistic(value):
    nums = [int(i) ** len(str(value)) for i in str(value)]
    return value == sum(nums)