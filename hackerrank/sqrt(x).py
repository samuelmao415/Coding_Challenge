#Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

#Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
x = 8
increments = 1
output = _
while (increments) **2 <=x:
    output = increments
    increments = increments + 1

output



class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        increments = 1
        output = 0
        while (increments) **2 <=x:
            output = increments
            increments = increments + 1

        return(output)
