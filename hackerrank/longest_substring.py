import time
s="abcabcbb"

s ="bbbbb"
s=''
len(s)

all([s[x-1]==s[x] for x,j in enumerate(s)])

s[1]
s[0:1]

def longest_substring(s):
    tic = time.clock()
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
            #print(s[beg_index:beg_index+needle], 'current_length:', current_length,'beg_index:', beg_index, 'needle: ', needle)
            needle +=1
            if current_length>max_length:
                max_length = current_length


    toc = time.clock()
    print((toc - tic)*1000)
    return(max_length)

s= "jpphtdynjkopydnebyjkwmcctoymhmzrdqyzuwofjewhhmokkxxglbie"
longest_substring(s)

s= "tmmzuxta"
longest_substring_faster(s)
def longest_substring_faster(s):
    tic = time.clock()
    used = {}
    max_length = start = 0 #start is the left side of the string
    for i, c in enumerate(s):
        print('-'*20)
        print(s[i:])
        if c in used and start <= used[c]:
            print('if loop.')
            print('c: ', c, 'used[c]: ', used[c], 'start: ', start)
            start = used[c] + 1
            print('start: ', start)
        else:
            print('else loop')
            max_length = max(max_length, i - start + 1)
            print('max_length: ', max_length, 'i: ', i, 'start: ', start)

        used[c] = i
        print('used: ', used, 'used[c]: ', used[c])

    toc = time.clock()
    #print((toc - tic)*1000)
    #print(used)
    return max_length
