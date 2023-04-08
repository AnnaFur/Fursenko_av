def leap_year(year):
    # your code here
    x = year
    if ((x % 4 == 0) and (x % 100 != 0)) or (x % 400 == 0):
        text_result = 'YOU SHALL PASS'
    else:
        text_result = 'YOU SHALL NOT PASS'
    return text_result

assert leap_year(5) == 'YOU SHALL NOT PASS'