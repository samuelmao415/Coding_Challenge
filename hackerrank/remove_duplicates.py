def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n=0

        while n < len(nums) -1 :
            if nums[n]==nums[n+1]:
                nums.remove(nums[n+1])
                #print(n,nums)
                n = n - 1
            n=n+1

        return(len(nums))
                
