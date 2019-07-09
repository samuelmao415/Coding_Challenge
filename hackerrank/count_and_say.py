number = 1211
number = 111221

#number = str(number)
countAndSay(5)
def countAndSay(n):
    res = "1"
    for _ in range(n-1):
        res = helper(res)
    return res

helper(number)
def helper(n):
    n = str(n)
    count, i, res = 1, 0, ""
    #print('res beginning', res)
    while i < len(n) - 1:
        if n[i] == n[i+1]:
            count += 1
        else:
            res += str(count) + n[i]
            #print('res inside:', res)
            #print('n[i]: ', n[i], 'i: ',i)
            count = 1
        i += 1
    #print('res outside upper', res, 'i: ', i )
    res += str(count) + n[i]
    #print('res outside lower', res)
    return res
