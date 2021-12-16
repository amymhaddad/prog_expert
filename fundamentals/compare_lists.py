def compare_lists(lst1=[], lst2=[]):
    unique_nums = set()
    for i, num1 in enumerate(lst1):
        for k, num2 in enumerate(lst2):
            if num1 == num2 and num1 not in unique_nums:
                unique_nums.add(num1)
    return len(unique_nums)

