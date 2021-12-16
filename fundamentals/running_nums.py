def running_sums(nums):
    prev = nums[0]
    new_list = len(nums) * [None]
    for i in range(1, len(nums)-1, 1):
        curr = nums[i]+ nums[i-1]
        new_list[i] = curr
        prev = curr
    return new_list
    # new_list = len(nums) * [None]
    # prev = nums[0]
    # new_list[0] = prev
    #
    # for i in range(1, len(nums), 1):
    #
    #     prev += nums[i]
    #     new_list[i] = prev
    # return new_list
    
print(running_sums([5, 4, 2, 1, 5, 6, 4]))
