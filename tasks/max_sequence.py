def max_sequence(arr):
    result = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            continue
        summ = arr[i]
        for j in range(i + 1, len(arr)):
            summ += arr[j]
            if summ > result:
                result = summ
    return result


# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c
# Пока не проходят некоторые тесты? Думаю над оптимизацией
