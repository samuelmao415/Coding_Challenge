s = "babad"
s = "abb"

s_rev = s[::-1]

s1 = 'abba'
s2 = 'abbd'

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_rev = s[::-1]
        if s_rev == s:
            return(s)



        max_length =0
        current_length =0
        terminal = 0 #left side of s_rev
        slide = 1 #slide to the right of s_rev

        max_list=[]
        while terminal + slide <=len(s) :
            if s_rev[terminal:terminal + slide] in s:

                if s_rev[terminal:terminal + slide] == s_rev[terminal:terminal + slide][::-1]:
                    #print('s_rev',s_rev[terminal:terminal + slide])
                    max_list.append(s_rev[terminal:terminal + slide])
                    #print('list',max_list)

                current_length +=1
                slide +=1
                if current_length>max_length:
                    max_length = current_length

            else:
                terminal +=1
                slide = 1
                current_length = 0

        #print('max_list:',  max_list)

        return(sorted(max_list, key = lambda x:len(x))[-1])
                
