class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)

        return res


"""
        intervals.sort(key=lambda x: x[1])
        #sort by intervals that end earliest

        previous_end = float("-inf")

        #intervals to remove default ot length
        remove = len(intervals)

        for start, end in intervals:

            if previous_end<=start: #no overlap
                remove-=1
                previous_end = end #basically skipping
        return remove
"""

        #remove interval that ends later to minimize chance of overlap!

