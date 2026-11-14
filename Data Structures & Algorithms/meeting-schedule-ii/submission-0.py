"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        start = sorted(i.start for i in intervals)
        end = sorted(i.end for i in intervals)

        best = 0
        count = 0
        l,r = 0,0

        while l < len(start) and r < len(end):
            if start[l] < end[r]:
                l+=1
                count+=1
            else:
                r+=1
                count-=1
            best = max(best, count)
        return best
#at point in time keep track of num meeting rooms and compare to max 
# start and end times list 
        