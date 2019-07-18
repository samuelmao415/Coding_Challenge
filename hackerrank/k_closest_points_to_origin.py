points = [[1,3],[-2,2]]
k = 1

sorted(points, key =sort_by_sum(points))
sorted(points, reverse = True, key = lambda x: x[0]*x[0] + x[1]*x[1])[:2]


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        return(sorted(points, key = lambda x: x[0]*x[0] + x[1]*x[1])[:K])
