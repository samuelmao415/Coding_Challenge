class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key= lambda x: x[0])
        if len(intervals) <2:
            return(intervals)
        output = []
        i = 0
        while i <=len(intervals)-1:
            if i==len(intervals)-1:
                output.append(intervals[i])
                break

            start, end = intervals[i][0], intervals[i][1]
            while i<len(intervals)-1 and end >= intervals[i+1][0] :
                end =  max(end,intervals[i+1][1])
                i += 1

            output.append([start,end])
            i +=1

        return(output)
                
