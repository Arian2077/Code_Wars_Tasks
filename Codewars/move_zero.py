def move_zeros(lst):
    new_list = []
    zero_count = 0
    for num in lst:
        if num != 0:
            new_list.append(num)
        else:
            zero_count += 1
            
    new_list.extend([0] * zero_count)
    
    return new_list