
def findNumber(arr, k):
    yes_length =0
    for i in range(len(arr)):
        if k == arr[i]:
            yes_length += 1
        else:
            continue
    if yes_length >0:
        return('YES')
    else:
        return('NO')
arr = [5,1,2,3,4,5,1]
k = 2
findNumber(arr, k)
