
s = "{[]}"
s = "()[]{}"
s = "(]"
s="(([]){})"
s = "([[][]{({}({}))}])"


isValid(s)
def isValid(s):
    bracket_array = ['()','{}','[]']
    str_length = len(s)
    n = 0
    while n<=str_length:
        for i in bracket_array:
            if i in s:
                s = s.replace(i,'')
        n=n+1
    if s == '':
        return(True)
    else:
        return(False)
