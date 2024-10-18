def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    base_num = 0
    num_list = []
    for i in range(n):
        base_num += x
        num_list.append(base_num)
    return num_list