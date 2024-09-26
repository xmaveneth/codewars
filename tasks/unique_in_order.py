def unique_in_order(sequence):
    if sequence:
        return [sequence[0]] + [sequence[i] for i in range(1, len(sequence)) if sequence[i] != sequence[i - 1]]
    return []


# https://www.codewars.com/kata/54e6533c92449cc251001667