#Sol 1
def odds(nums):
    odd_nums = []

    for num in nums:
        if num % 2 != 0:
            odd_nums.append(num)
    return odd_nums 

#Sol 2
def odds(nums):
    return [num for num in nums if num %2 != 0 ]
