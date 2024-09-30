def domain_name(url: str):
    if url.startswith('http'):
        url = url.split('://')[1]
    for i in url.split('.'):
        if i != 'www':
            return i


# https://www.codewars.com/kata/514a024011ea4fb54200004b
