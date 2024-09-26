def to_camel_case(text: str):
    if text:
        text = text.replace('-', ' ').replace('_', ' ')
        result = [el if i == 0 else el.capitalize() for i, el in enumerate(text.split())]
        return ''.join(result)
    return ''


# https://www.codewars.com/kata/517abf86da9663f1d2000003