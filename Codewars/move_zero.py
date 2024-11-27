<<<<<<< HEAD
def move_zeros(lst):
    new_list = []
    zero_count = 0
    for num in lst:
        if num != 0:
            new_list.append(num)
        else:
            zero_count += 1
            
    new_list.extend([0] * zero_count)
    
=======
def move_zeros(lst):
    new_list = []
    zero_count = 0
    for num in lst:
        if num != 0:
            new_list.append(num)
        else:
            zero_count += 1
            
    new_list.extend([0] * zero_count)
    
>>>>>>> 8267eb5b08f297691c348ec76d94ab0d97dd17ed
    return new_list