intervals = [[0, 30],[5, 10],[15, 20]]


sorted(intervals, key= lambda x: x[0])



l = []
for i in intervals:
    l.append((i[0],1))
    l.append((i[1],-1))

l
l.sort()
l

rooms, available = 0,0
for time,sign in l:
    if sign ==1:
        if available ==0:
            rooms +=1
        else:
            available -=1
    else:
        available +=1



class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        l = []
        for i in intervals:
            l.append((i[0],1))
            l.append((i[1],-1))
        l.sort()

        rooms, available = 0,0
        for time,sign in l:
            if sign ==1:
                if available ==0:
                    rooms +=1
                else:
                    available -=1
            else:
                available +=1
    
