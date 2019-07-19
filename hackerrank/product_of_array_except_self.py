nums = [1,2,3,4]

nums[2:]
nums[:0] + nums[1:]
list(range(4,-1,-1))


x*nums[:3]

productExceptSelf_slow(nums)
 def productExceptSelf_slow(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #product_list = []
        nums_copy = nums[:]
        for i, num in enumerate(nums):
            list_for_product = nums[:i] + nums[i+1:]
            product =1
            for number_in_product in list_for_product:
                product = number_in_product*product
            nums_copy[i] = product
            #print(nums_copy[i])
        return(nums_copy)

nums = [1,2,3,4]
productExceptSelf_faster(nums)
def productExceptSelf_faster(nums):
    product_list = [1]*len(nums)
    previous_product =1
    #left side
    for i in range(0,len(nums)):
        product_list[i] = previous_product
        previous_product = previous_product * nums[i]
    #right_side
    previous_product =1
    for i in range(len(nums)-1,-1,-1):
        product_list[i] = previous_product * product_list[i]
        previous_product = previous_product * nums[i]

    return(product_list)
