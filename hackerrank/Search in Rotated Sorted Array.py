nums = [4,5,6,7,0,1,2]
nums = [5,6,7,1,2,3,4]
target = 0

high_index = len(nums)-1
low_index = 0

while low_index < high_index:
    mid_index = (high_index + low_index)//2
    if nums[mid_index] == target:
        return(mid_index)

    if (target >nums[mid_index]) ^ (target < nums[-1]) ^ (nums[0]>nums[mid_index]>target) :
        low_index = mid_index +1
    else:
        high_index = mid_index


0//2
