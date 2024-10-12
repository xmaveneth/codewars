def find_uniq(arr):
    set_lst = list(set(arr))
    some_res = arr[:3]
    if some_res[0] == some_res[1] == some_res[2]:
        return set_lst[1] if set_lst[0] == some_res[0] else set_lst[0]
    else:
        return set_lst[0] if some_res.count(set_lst[0]) == 1 else set_lst[1]

# https://www.codewars.com/kata/585d7d5adb20cf33cb000235
