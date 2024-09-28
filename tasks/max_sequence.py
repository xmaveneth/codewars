def max_sequence(arr):
    result = 0
    cur_result = 0
    for el in arr:
        cur_result += el
        result = max(result, cur_result)
        cur_result = max(cur_result, 0)
    return result


# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c
# Удалось оптимизировать алгоритмом Кадана. Сложность O(n)
