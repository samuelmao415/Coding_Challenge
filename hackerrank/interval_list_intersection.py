A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]

res = []
i,j =0,0
while i < len(A) and j<len(B):
    if max(A[i][0],B[j][0])<=min(A[i][1],B[j][1]):
        res.append([max(A[i][0],B[j][0]),min(A[i][1],B[j][1])])
    if A[i][1]>B[j][1]:
        j+=1
    else:
        i+=1




res


# for x in list(zip(A,B)):
#     res.append([max(x[0][0],x[1][0]),min(x[0][1],x[1][1])])
