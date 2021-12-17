def replace(lst, target, swap_value):

    for i in range(len(lst)):
        curr_word = lst[i]
        if curr_word == target:
            lst[i] = swap_value
    return lst

