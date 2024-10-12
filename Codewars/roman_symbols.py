def solution(n):
    if not 1 <= n <= 3999:
        return "Input must be between 1 and 3999"

    roman_symbols = [
        ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
        ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
        ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)
    ]

    result = ""
    for symbol, value in roman_symbols:
        while n >= value:
            result += symbol
            n -= value

    return result