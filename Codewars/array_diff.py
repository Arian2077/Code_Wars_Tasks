def array_diff(a, b):
    new = []
    for num in a:
        if num not in b:
            new.append(num)  
    return new