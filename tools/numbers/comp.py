# tools/numbers/comp.py

def sumofdigits(number):
    digits = [int(digit) for digit in str(number)]
    return sum(digits)

def ispal(number):
    str_number = str(number)
    return str_number == str_number[::-1]
