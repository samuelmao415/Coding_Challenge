digits = [1,2,3]


digits = [str(d) for d in digits]
digits = ''.join(digits)
digits = int(digits) +1
list(str(digits))


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = [str(d) for d in digits]
        digits = ''.join(digits)
        digits = int(digits) +1
        return(list(str(digits)))
