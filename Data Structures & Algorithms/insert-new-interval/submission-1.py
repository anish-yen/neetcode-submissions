class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        #start = newInterval[0]
        #end = newInterval[1]

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: # no overlap, end of new before start
                res.append(newInterval)
                return res + intervals[i:]

            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i]) # if no overlap and after- so append

            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        res.append(newInterval)
        return res

        #dont sort in place just get new res
        # if start_new > end no overlap # check start first
        # if end_new less end no over lap
        # else change new interval andappend to res # any other case