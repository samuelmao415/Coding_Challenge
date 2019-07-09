s = 'Hello World'
s = 'Hello some asdw'
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return(0)
        if len(s)>0:
            s = s.rstrip()
            s_list = s.split(' ')
            last_word = s_list[-1]
            return(len(last_word))
        
