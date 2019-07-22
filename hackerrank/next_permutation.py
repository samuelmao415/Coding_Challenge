nums = [1,2,3]


nums[:len(nums)-2] + [nums[-1]] + [nums[-2]]


nums = [1,3,2,1] # --> 2,1,1,3
nums = [5,3,4,2,8,9,2] # -->
nums = [2,1,3] # --> 231
nums = [1,5,8,4,7,6,5,3,1]
nums = [2,2,7,5,4,3,2,2,1]
nums
nums
# nums[n:] = sorted(nums[n:])
if nums == sorted(nums, reverse=True): #equals to largest
    nums = nums.sort()
elif nums == sorted(nums): #equals to smallest
    nums[-1], nums[-2] = nums[-2], nums[-1] #swap the last two digits
else:
    n = -1
    needle = len(nums) -1
    while nums[n] <= nums[n-1]:
        print(nums[n], nums[n-1])
        n -=1
        #break
    print(nums[n-1:])
    while needle >0:
        if nums[needle] > nums[n-1]:
            nums[n-1],nums[needle] = nums[needle], nums[n-1]
            print('nums[n-1]:', nums[n-1])
            break
        else:
            needle -=1
            print('needle: ', needle)
    nums[n:] = sorted(nums[n:])


print(nums)
