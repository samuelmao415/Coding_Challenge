
# variable l is current left parenthesis count

# variable r is current right parenthesis count

# l - r < 0 means this is not a valid parenthesis

n=2
res = []
s = [("(", 1, 0)]
# test = s.pop()

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        bracket_left_right = [('(',1,0)]
        combination = []

        while bracket_left_right:
            b, l, r = bracket_left_right.pop()
            if l-r <0 or l>n or r>n:
                continue
            if l==r and l ==n:
                combination.append(b)
            bracket_left_right.append((b+'(', l+1,r))
            bracket_left_right.append((b+')', l,r+1))

        return(combination)
