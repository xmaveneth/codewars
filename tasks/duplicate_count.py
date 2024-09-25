def duplicate_count(text: str):
    text = text.lower()
    return sum([1 if text.count(i) > 1 else 0 for i in set(text)])

# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
