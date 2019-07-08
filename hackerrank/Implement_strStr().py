haystack = "hello"
needle = "ll"

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return(0)

        if needle in haystack:
            needle_length = len(needle)
            for index in range(len(haystack)):
                if needle == haystack[index:needle_length+index]:
                    return(index)
        else:
            return(-1)
