def make_readable(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    seconds = seconds % 60
    return f"{str(hours).rjust(2, '0')}:{str(minutes).rjust(2, '0')}:{str(seconds).rjust(2, '0')}"


# https://www.codewars.com/kata/52685f7382004e774f0001f7
