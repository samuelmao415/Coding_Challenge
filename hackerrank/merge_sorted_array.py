nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

nums1[m:] = nums2

nums1
nums1.sort()
sorted

nums1 + nums2

nums1 = sorted(sorted(nums1)[-m:]+ sorted(nums2)[-n:])

nums1


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        return(nums1.sort())
