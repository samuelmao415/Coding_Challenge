class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            for index in range(len(nums)):
                if target == nums[index]:
                    return(index)
        else:
            nums.append(target)
            nums = sorted(nums)
            for index in range(len(nums)):
                if target == nums[index]:
                    return(index)
