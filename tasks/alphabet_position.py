def alphabet_position(text):
    alpha = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    return ' '.join([str(alpha.index(i) + 1) for i in text.lower() if i in alpha])

# https://www.codewars.com/kata/546f922b54af40e1e90001da
