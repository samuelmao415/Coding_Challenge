# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# Given
nums = [11, 15,2, 7,5,2,5]
target = 9

nums[2:]

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#



twoSum(nums,target)

#smarter solution
def twoSum(nums,target):
    result = {}
    for index, value in enumerate(nums):
        if target - value in result:
            index_one = index
            index_two = result[target-value]
        result[value] = index
    return(index_one, index_two)




#dumber  solution
def twoSum(nums,target):
    number_one, number_two = float('-inf'), float('-inf')
    number_one_index, number_two_index = float('-inf'), float('-inf')
    for index, number in enumerate(nums):
        if target - number in nums[index+1:]:
            number_two = target - number
            number_one = number
            number_one_index = index
            for index, number in enumerate(nums[index+1:]):
                if number == number_two:
                    number_two = number
                    number_two_index = index + number_one_index +1
    print('number_one', number_one)
    print('number_one_index', number_one_index)
    print('number_two',number_two)
    print('number_two_index', number_two_index)
    return(number_one_index, number_two_index)
