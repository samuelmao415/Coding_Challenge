s="abcabcbb"

s ="bbbbb"
s=''
len(s)

all([s[x-1]==s[x] for x,j in enumerate(s)])

s[1]
s[0:1]

def longest_substring(s):
    if len(s) ==0:
        return(0)
    if all([s[x-1]==s[x] for x,j in enumerate(s)]):
        return(1)

    max_length, current_length = 0, 1
    beg_index=0
    needle = 1
    while beg_index<len(s)-needle:
        if s[beg_index+needle] in s[beg_index:beg_index+needle]:
            beg_index +=1
            current_length = 1
            needle =1
        else:
            current_length +=1
            print(s[beg_index:beg_index+needle], 'current_length:', current_length,'beg_index:', beg_index, 'needle: ', needle)
            needle +=1
            if current_length>max_length:
                max_length = current_length



    return(max_length)

s= "jpphtdynjkopydnebyjkwmcctoymhmzrdqyzuwofjewhhmokkxxglbie"
longest_substring(s)
