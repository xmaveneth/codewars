def dir_reduc(arr):
    arr = ' '.join(arr)
    while 'NORTH SOUTH' in arr or 'SOUTH NORTH' in arr or 'EAST WEST' in arr or 'WEST EAST' in arr or '  ' in arr:
        arr = arr.replace('NORTH SOUTH', '').replace('SOUTH NORTH', '').replace('EAST WEST', '').replace('WEST EAST', '').replace('  ', ' ')
    return arr.split()


# https://www.codewars.com/kata/550f22f4d758534c1100025a
