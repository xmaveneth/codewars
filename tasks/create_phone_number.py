def create_phone_number(n):
    n = list(map(str, n))
    return f"({''.join(n[:3])}) {''.join(n[3:6])}-{''.join(n[6:])}"

# https://www.codewars.com/kata/525f50e3b73515a6db000b83