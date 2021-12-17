#Sol 1
def running_sums(nums):
    new_list = len(nums) * [None]
    prev = nums[0]
    new_list[0] = prev

    for i in range(1, len(nums), 1):
        prev += nums[i]
        new_list[i] = prev
    return new_list

#Sol 2
def running_sums(nums):
    new_nums = []
    total = 0

    for num in nums:
        total += num 
        new_nums.append(total)
    return new_nums
