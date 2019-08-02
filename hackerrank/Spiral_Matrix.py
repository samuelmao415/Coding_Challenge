matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

matrix.pop(0)

[*matrix.pop(0)]

[*matrix.pop(0)]

123 69 87,45

[*zip(*matrix)][::-1].pop(0)


[*zip(*matrix)][::-1].pop(0)
def spiral_recusion(mtx):
    #res = [*mtx.pop(0)]
    return mtx and  [*mtx.pop(0)] +spiral_recusion([*zip(*mtx)][::-1])


# x and y: if x is false, then x, else y
spiralOrder(matrix)

spiral_recusion(matrix)
    #[*zip(*matrix)][::-1].pop(0)


zip(*B)[::-1]
A ='asdasnot empty'
B =''
A and B



class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        while matrix:
            res.extend(matrix.pop(0))
            matrix = zip(*matrix)[::-1]

        return(res)
            
