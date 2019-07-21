#(nums[mid_index]<nums[0]<=target):
nums = [7,8,0,2,3,5]
target = 8
#(target <=nums[mid_index]<nums[0])
nums = [2,3,4,5,0,1]
#(nums[0]<=target<nums[mid_index])
nums = [0,1,2,3,4,5,6]

target =3

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        high_index = len(nums)-1
        low_index = 0

        while low_index <= high_index:
            mid_index = (high_index + low_index)//2
            print(mid_index)
            if nums[mid_index] == target:
                return(mid_index)
            if (nums[0]<=target<nums[mid_index]) or (target <=nums[mid_index]<nums[0]) or (nums[mid_index]<nums[0]<=target):
                high_index = mid_index - 1
            else:
                low_index = mid_index +1

        return(-1)
