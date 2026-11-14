class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        start = newInterval[0]
        end = newInterval[1]

        if end < intervals[0][1]:
            intervals.insert(0, newInterval)
            return intervals
        
        if start > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals
            
        res = []
        for i in range(1, len(intervals)):
            #overlap
            if start < intervals[i-1][1] and end > intervals[i][0]:
                #print(start, intervals[i-1][1], end, intervals[i][0])
                res.append([ min(start, intervals[i-1][0]), max(end, intervals[i][1])  ])
            #nonoverlap
            elif start> intervals[i-1][1] and end < intervals[i][0]:
                intervals.insert(i, newInterval)
                return intervals
        return res