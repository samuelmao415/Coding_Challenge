nums = [1,1,1]
nums = [1,2,1,1]
k=2
nums = [1]
k=1
nums = [1,2,3]
k= 3
nums = [100,1,2,3,4]
k = 6
nums = [0,0,0,0,0,0,0,0,0,0]
k = 0
nums = [1,3,4,13]
k=7

sum_dict = {0:1}
subs = 0
current_sum = 0
for n in nums:
    current_sum +=n
    subs += sum_dict.get(current_sum - k,0)
    sum_dict[current_sum] = sum_dict.get(current_sum,0) + 1

subs            













#dict.get(key,value): value is optional. it's the value to be returned if key is not found
# sums = {0:1} # prefix sum array
# res = s = 0
# for n in nums:
#     s += n # increment current sum
#
#     print('n: ',n,'s: ',s, 'k: ', k, 's-k: ', s-k)
#
#     res += sums.get(s - k, 0) # check if there is a prefix subarray we can take out to reach k
#
#     print('sums.get(s - k, 0): ', sums.get(s - k, 0))
#     print('sums.get(s, 0): ', sums.get(s, 0))
#
#     sums[s] = sums.get(s, 0) + 1 # add current sum to sum count #update dic with key s with value 0+1
#
#     print('*'*20)

res
sums
sums[11] = sums.get(11,2) +1
sums
#slow:
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 1 and nums[0] == k:
            return(1)
        n = 0
        needle = 1
        subs = 0
        while n <len(nums):
            if sum(nums[n:n+needle]) !=k and n+needle <=len(nums):
                #print(nums[n:n+needle])
                needle +=1
                #print(needle)
            elif sum(nums[n:n+needle]) ==k and n+needle <=len(nums):
                subs +=1
                #print('needle reset')
                needle +=1
                #n+=1
            else:
                n+=1
                needle = 1
        return(subs)
