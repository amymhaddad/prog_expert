# Sol 1 - Start at the beginning of list and go to (but don't include) len(lst) - elements_to_trim
def trim_list(lst, elements_to_trim):
    return lst[: len(lst) - elements_to_trim]


# Sol 2
def trim_list(lst, elements_to_trim):
    return [lst[i] for i in range(len(lst) - elements_to_trim)]


# Sol 2 - loop through all elements -- except for the ones at the end; just loop through the elements I want to return
def trim_list(lst, elements_to_trim):
    new_list = []

    for i in range(len(lst) - elements_to_trim):
        new_list.append(lst[i])
    return new_list


# Sol 3
def trim_list(lst, elements_to_trim):

    new_list = []

    while elements_to_trim > 0:
        lst.pop()
        elements_to_trim -= 1

    for ele in lst:
        new_list.append(ele)
    return new_list
