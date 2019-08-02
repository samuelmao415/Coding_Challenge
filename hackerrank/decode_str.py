

s = "2[abc]3[cd]ef"


lis = [['',1]]
num = ''
for i in s:
    if i.isdigit():
        num+=i
    elif i =='[':
        lis.append(['',int(num)])
        num = ''
    elif i==']':
        alpha, digit = lis.pop()
        lis[-1][0]+=alpha*digit
    else:
        lis[-1][0] +=i
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        lis = [['',1]]
        num = ''
        for i in s:
            if i.isdigit():
                num+=i
            elif i =='[':
                lis.append(['',int(num)])
                num = ''
            elif i==']':
                alpha, digit = lis.pop()
                lis[-1][0]+=alpha*digit
            else:
                lis[-1][0] +=i

        return(lis[0][0])
