
lst = [1,2,3]

def permutation(lst):
# If lst is empty then there are no permutations
    if len(lst) == 0:
        return []
    # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        print('lst length 1: ', lst)
        return [lst]
    l = []
    print('looping lst:', lst)
    for i in range(len(lst)):
       print('i:', i)
       individual_number = lst[i]
       print('extracted:', individual_number)
       # Extract lst[i] or individual_number from the list. remLst is remaining list
       remLst = lst[:i] + lst[i+1:]
       # Generating all permutations where individual_number is first element
       print('remLst', remLst)
       for p in permutation(remLst):
           print("extracted: ", individual_number,", p returned:",p)
           l.append([individual_number] + p)
           print('l:', l)
    print('returning l:', l)
    return l


permutation(lst)


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <=1:
            return([nums])
        answer = []
        for i, num in enumerate(nums):
            head = nums[i]
            remaining = nums[:i] + nums[i+1:]
            for res in self.permute(remaining):
                answer.append([head] + res)
        return(answer)
        
