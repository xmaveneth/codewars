def find_outlier(integers):
    odd_nums = []
    even_nums = []

    for el in integers:
        if el % 2:
            odd_nums.append(el)
        else:
            even_nums.append(el)
        if odd_nums and even_nums and len(odd_nums + even_nums) > 2:
            break
    return odd_nums[0] if len(odd_nums) == 1 else even_nums[0]

# https://www.codewars.com/kata/5526fc09a1bbd946250002dc