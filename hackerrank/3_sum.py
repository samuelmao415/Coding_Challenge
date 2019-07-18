#https://leetcode.com/problems/3sum/discuss/232712/Best-Python-Solution-(Explained)
solution = (
  (-1, 0, 1),
  (-1, -1, 2),
  (0, -1, 1))

nums = [-1, 0, 1, 2, -1, -4]
for i in range(len(nums)-2):
    print(i)
#accepted:
def threeSum(self, nums):
    res = []
    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]: continue#avoid duplicate
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l +=1
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1; r -= 1
    return res








#time limit exceeded
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        if all(num == 0 for num in nums):
            return [[0,0,0]]
        if all([num <=0 for num in nums]):
            return []
        if all([num >=0 for num in nums]):
            return []
        found = []
        nums.sort()
        rightmost = len(nums)-1
        index=0
        #Fix the first element, then search for the other two
        while nums[index]<=0:
            left = index + 1
            right = rightmost

            while left < right:
                check_sum = (nums[index] + nums[left] + nums[right])

        #Since the list is sorted, we can check whether the leftmost or the rightmost element is causing the sum!=0
                if check_sum == 0:
                    new_found = [nums[index], nums[left], nums[right]]
                    if new_found not in found:
                        found.append(new_found)

        #even if we find the element, we need to decrease right, to find all other pairings with the first number
                    right -=1
                    left += 1

        #if the sum is less than 0, then our 2nd number is too low, we check the next highest one in our sorted list
                elif check_sum < 0:
                    left += 1

        #if the sum is less than 0, then our 3rd number is too high, we check the next lowest one in our sorted list
                else:
                    right -= 1
            index +=1

        return found
