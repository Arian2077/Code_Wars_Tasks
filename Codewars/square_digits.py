def square_digits(num):
    digit_str = str(num)
    squared_digits = ''.join(str(int(digit) ** 2) for digit in digit_str)
    return int(squared_digits)

