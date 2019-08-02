num_dict={'0':'','1':'','2':'abc','3':'def','4': 'ghi', '5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

digits = '23'

cmb = ['']

for digit in digits:
    cmb = [i+j for i in cmb for j in num_dict[digit] ]




class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits:
            num_dict={'0':'','1':'','2':'abc','3':'def','4': 'ghi', '5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}



            cmb = ['']

            for digit in digits:
                cmb = [i+j for i in cmb for j in num_dict[digit] ]

            return(cmb)
        else:
            return digits
