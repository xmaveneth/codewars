def is_valid_walk(walk: list):
    if len(walk) == 10:
        if walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w'):
            return True
    return False


# https://www.codewars.com/kata/54da539698b8a2ad76000228
