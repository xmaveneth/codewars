def tribonacci(signature, n):
    if n >= len(signature):
        while len(signature) != n:
            signature.append(sum(signature[-3:]))
    return signature[:n]


# https://www.codewars.com/kata/556deca17c58da83c00002db
