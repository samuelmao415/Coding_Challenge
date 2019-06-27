nums = [-2,1,-3,4,-1,2,1,-5,4]
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        start = 0
        combination_list = []
        while start < length:
            for ind, val in enumerate (nums):
                list = nums[start:start + ind+1]
                combination_list.append((list,sum(list)))
            start = start + 1

        output = sorted(combination_list, key = lambda x: x[1], reverse = True)[0][1]
        return(output)


nums = [-2,1,-3,4,-1,2,1,-5,4]
maxSubArray(nums)



nums=[-2,1,-3,4,-1,2,1,-5,4]
nums = [8,-19,5,-4,20]
nums = [-8,-19,-5,-4,-20,-1,-13,-2]
maxSubArrays(nums)
def maxSubArrays(nums):
    max_value, current_sum = float('-inf'), 0
    for number in nums:
        if current_sum + number <0:
            max_value, current_sum = max(max_value, current_sum + number), 0
        else:
            max_value, current_sum = max(max_value,current_sum + number), current_sum + number
    return(max_value)
