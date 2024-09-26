import string
def is_pangram(st):
    return all(map(lambda x: x in st.lower(), string.ascii_lowercase))


# https://www.codewars.com/kata/545cedaa9943f7fe7b000048
