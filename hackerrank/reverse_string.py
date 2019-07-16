


s= ["h","e","l","l","o"]
reverseString(s)
def reverseString(s):
    original_len= len(s)
        #s= [s[-i-1] for i,x in enumerate(s)]
    holder = '_'
    for i in range(len(s)):
        s.append(holder)

    for i in range(original_len):
        s[original_len + i] = s[original_len-i -1]


    del s[:original_len]  #delete my index
    return(s)
