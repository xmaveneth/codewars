def generate_hashtag(s: str):
    new_s = '#' + ''.join(s.title().split())
    if len(s) == 0 or len(new_s) > 140:
        return False
    return new_s


# https://www.codewars.com/kata/52449b062fb80683ec000024
