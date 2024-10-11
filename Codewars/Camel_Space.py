def solution(s):
    if not s:
        return s
    result = [s[0].lower()]
    for char in s[1:]:
        if char.isupper():
            result.append(' ')
            result.append(char)
        else:
            result.append(char)
    return ''.join(result)